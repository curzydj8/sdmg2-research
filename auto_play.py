"""自主游戏主循环"""
import subprocess
import time
import os
from datetime import datetime, timedelta

# 配置
PID = 77327
WID_CMD = "DISPLAY=:99 xdotool search --pid 77327 | tail -1"
SSH = "ssh -F ~/.ssh/config zhang-new"

def ssh_cmd(cmd):
    result = subprocess.run(f"{SSH} '{cmd}'", shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_wid():
    return ssh_cmd(WID_CMD)

def screenshot(name):
    wid = get_wid()
    ssh_cmd(f"DISPLAY=:99 xwd -id {wid} 2>/dev/null | xwdtopnm 2>/dev/null | pnmtopng 2>/dev/null > /tmp/xvfb-test/auto/screenshots/{name}.png")

def press_key(key):
    wid = get_wid()
    ssh_cmd(f"DISPLAY=:99 xdotool key --window {wid} {key}")

# 主循环
start_time = datetime.now()
end_time = start_time + timedelta(hours=2)
games_completed = 0

print(f"开始时间: {start_time}")
print(f"结束时间: {end_time}")
print(f"实例 PID: {PID}")

# 初始化：关闭信息屏
wid = get_wid()
print(f"窗口 ID: {wid}")
ssh_cmd(f"DISPLAY=:99 xdotool windowactivate --sync {wid}")
time.sleep(1)
press_key("Return")
time.sleep(3)

# 游戏循环
while datetime.now() < end_time and games_completed < 100:
    try:
        # 截图
        screenshot(f"game_{games_completed}")
        
        # 上分
        press_key("5")
        time.sleep(3)
        
        # 尝试下注（Joystick 模式）
        # Bet = BUTTON2, 尝试常见映射
        for key in ["LeftAlt", "x", "z"]:
            press_key(key)
            time.sleep(2)
        
        games_completed += 1
        print(f"完成局数: {games_completed}, 时间: {datetime.now()}")
        
        # 简单延时，避免过快
        time.sleep(5)
        
    except Exception as e:
        print(f"错误: {e}")
        time.sleep(10)

print(f"结束. 完成局数: {games_completed}")
