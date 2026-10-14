"""24小时自主运行监督器"""
import subprocess
import time
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from learning.checkpoint import CheckpointManager
from learning.controller import AutonomousLearningController

SSH = "ssh -F /home/hatch/.ssh/config zhang-new"
PROTECTED_PID = 36644
START_TIME = datetime.now()
import fcntl
LOCK_FILE = "/tmp/sdmg2-supervisor.lock"
_lock_fh = open(LOCK_FILE, "w")
try:
    fcntl.flock(_lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    print("另一个监督器正在运行，退出")
    sys.exit(0)

TARGET_HOURS = 24

def ssh(cmd):
    r = subprocess.run(f"{SSH} '{cmd}'", shell=True, capture_output=True, text=True, timeout=30)
    return r.stdout.strip()

def check_protected():
    """确认原始实例受保护"""
    out = ssh(f"ps -p {PROTECTED_PID} -o pid 2>&1 | tail -1")
    return str(PROTECTED_PID) in out

def get_mame_pid():
    """获取测试实例 PID（重试 3 次）"""
    for _ in range(3):
        try:
            out = ssh("pgrep -f 'mame.*24h' | head -1")
            pid = out.strip().split()[0] if out.strip() else ""
            if pid and pid.isdigit():
                # 二次确认进程确实存在且是我们的实例
                check = ssh(f"ps -p {pid} -o args | grep -q '24h' && echo OK")
                if "OK" in check:
                    return pid
        except Exception as e:
            print(f"检测异常: {e}")
        time.sleep(5)
    return None

def count_mame():
    """统计实例数量"""
    try:
        out = ssh("ps aux | grep 'nvram_directory /tmp/xvfb-test/24h' | grep -v grep | wc -l")
        return int(out.strip())
    except:
        return 0

def start_mame():
    """启动隔离实例"""
    ssh("rm -rf /tmp/xvfb-test/24h; mkdir -p /tmp/xvfb-test/24h/{config,nvram,screenshots,logs}")
    ssh("""cat > /tmp/xvfb-test/24h/config/sdmg2754ca.cfg <<'CFG'
<?xml version="1.0"?>
<mameconfig version="10">
    <system name="sdmg2754ca">
        <dipswitch tag="DSW2" mask="64" value="0" />
    </system>
</mameconfig>
CFG""")
    ssh("export DISPLAY=:99; setsid /usr/games/mame sdmg2754ca -rompath /home/zhangdawei/roms -window -cfg_directory /tmp/xvfb-test/24h/config -nvram_directory /tmp/xvfb-test/24h/nvram > /tmp/xvfb-test/24h/logs/mame.log 2>&1 < /dev/null &")
    time.sleep(15)
    return get_mame_pid()

def main():
    cp = CheckpointManager()
    ctrl = AutonomousLearningController()
    
    print(f"[{datetime.now()}] 监督器启动，目标 {TARGET_HOURS} 小时")
    
    mame_pid = None
    consecutive_failures = 0
    
    while True:
        elapsed = datetime.now() - START_TIME
        if elapsed > timedelta(hours=TARGET_HOURS):
            print(f"[{datetime.now()}] 达到 {TARGET_HOURS} 小时，继续运行...")
            # 不停止，继续
        
        # 1. 检查原始实例
        if not check_protected():
            print(f"[{datetime.now()}] 警告：原始实例 {PROTECTED_PID} 不存在！")
        
        # 2. 检查 MAME 实例
        mame_pid = get_mame_pid()
        if not mame_pid:
            consecutive_failures += 1
            print(f"[{datetime.now()}] MAME 未运行，重启 (失败 {consecutive_failures} 次)")
            cp.record_mame_exit("unknown", "not_running")
            
            if consecutive_failures > 5:
                print(f"[{datetime.now()}] 连续失败过多，降低频率")
                time.sleep(300)
                continue
            
            # 启动前再次确认无实例
            if count_mame() == 0:
                mame_pid = start_mame()
            else:
                mame_pid = get_mame_pid()
            if mame_pid:
                print(f"[{datetime.now()}] MAME 已启动 PID={mame_pid}")
                consecutive_failures = 0
            else:
                print(f"[{datetime.now()}] 启动失败")
                time.sleep(60)
                continue
        else:
            consecutive_failures = 0
        
        # 3. 保存检查点
        cp.data["last_state"] = {"mame_pid": mame_pid, "time": datetime.now().isoformat()}
        cp.save()
        
        # 4. 等待下一轮
        time.sleep(60)

if __name__ == "__main__":
    main()
