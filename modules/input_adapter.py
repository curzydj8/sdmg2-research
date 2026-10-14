#!/usr/bin/env python3
"""
统一输入接口 v2.0
基于 INPUT-RELIABILITY-REPORT.md：采用 uinput (evdev)，52% vs X11 6%
"""
import subprocess
import time
import os

class InputAdapter:
    """
    输入适配器：优先 uinput，X11 作为备用
    
    uinput 需要：
    - 用户在 input 组
    - /dev/uinput 权限 660，组 input
    - python3-evdev
    """
    
    # evdev 键码映射
    KEYMAP = {
        "5": "KEY_5", "1": "KEY_1",
        "a": "KEY_A", "b": "KEY_B", "c": "KEY_C", "d": "KEY_D",
        "e": "KEY_E", "f": "KEY_F", "g": "KEY_G", "h": "KEY_H",
        "i": "KEY_I", "j": "KEY_J", "k": "KEY_K", "l": "KEY_L",
        "m": "KEY_M", "n": "KEY_N",
        "Return": "KEY_ENTER", "space": "KEY_SPACE",
    }
    
    def __init__(self, wid="10485767", timeout=15, method="uinput"):
        self.wid = wid
        self.timeout = timeout
        self.method = method  # "uinput" or "x11"
        self.env_prefix = "export DISPLAY=:0; export XAUTHORITY=$(ls /run/user/1000/.mutter-Xwaylandauth.* 2>/dev/null | head -1); "
    
    def _ssh(self, cmd):
        full = f"ssh -F ~/.ssh/config zhang-new '{self.env_prefix}{cmd}'"
        try:
            r = subprocess.run(full, shell=True, capture_output=True, text=True, timeout=self.timeout)
            return True, r.stdout
        except subprocess.TimeoutExpired:
            return False, "TIMEOUT"
        except Exception as e:
            return False, str(e)[:100]
    
    def _press_uinput(self, key):
        """uinput 发送按键（52% 成功率）"""
        if key not in self.KEYMAP:
            return False, f"unknown key {key}"
        
        evdev_key = self.KEYMAP[key]
        # 在远程机上用 input 组运行
        py_code = f"""
from evdev import UInput, ecodes
import time
ui = UInput({{ecodes.EV_KEY: [ecodes.{evdev_key}]}}, name="sdmg2-auto")
time.sleep(0.3)
ui.write(ecodes.EV_KEY, ecodes.{evdev_key}, 1); ui.syn(); time.sleep(0.15)
ui.write(ecodes.EV_KEY, ecodes.{evdev_key}, 0); ui.syn(); time.sleep(0.2)
ui.close()
print("OK")
"""
        # 写临时脚本
        self._ssh(f"cat > /tmp/uinput-press.py << 'PYEOF'\n{py_code}\nPYEOF")
        ok, out = self._ssh("sudo -u zhangdawei -g input python3 /tmp/uinput-press.py 2>&1")
        if ok and "OK" in out:
            return True, "uinput sent (verify via screenshot)"
        return False, f"uinput failed: {out[:80]}"
    
    def _press_x11(self, key):
        """X11 备用（6% 成功率，仅备用）"""
        ok1, _ = self._ssh(f"xdotool keydown --window {self.wid} {key} 2>/dev/null")
        if not ok1:
            return False, "keydown failed"
        time.sleep(0.25)
        ok2, _ = self._ssh(f"xdotool keyup --window {self.wid} {key} 2>/dev/null")
        if not ok2:
            return False, "keyup failed (KEY MAY BE STUCK!)"
        return True, "x11 sent (verify via screenshot)"
    
    def press(self, key):
        """
        按一次键
        :return: (success: bool, message: str)
        调用者必须截图验证！
        """
        if self.method == "uinput":
            return self._press_uinput(key)
        else:
            return self._press_x11(key)
    
    def coin(self):
        """投币"""
        return self.press("5")
    
    def start(self):
        """开始"""
        return self.press("1")
    
    def discard(self, slot):
        """打出手牌 slot: 'a'-'n'"""
        if slot not in "abcdefghijklmn":
            return False, f"invalid slot {slot}"
        return self.press(slot)


if __name__ == "__main__":
    print("InputAdapter v2.0 (uinput primary, 52% vs X11 6%)")
