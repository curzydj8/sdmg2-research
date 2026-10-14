#!/usr/bin/env python3
"""截图模块 v1.0"""
import subprocess, time
from PIL import Image
import io

class ScreenReader:
    def __init__(self, wid="10485767", timeout=15):
        self.wid = wid
        self.timeout = timeout
        self.env_prefix = "export DISPLAY=:0; export XAUTHORITY=$(ls /run/user/1000/.mutter-Xwaylandauth.* 2>/dev/null | head -1); "
    
    def capture(self):
        """
        截屏
        :return: (PIL.Image or None, message)
        """
        cmd = f"ssh -F ~/.ssh/config zhang-new '{self.env_prefix}xwd -id {self.wid} 2>/dev/null | xwdtopnm 2>/dev/null | pnmtopng 2>/dev/null' > /tmp/sr.png"
        try:
            subprocess.run(cmd, shell=True, timeout=self.timeout, capture_output=True)
            img = Image.open("/tmp/sr.png").convert("RGB")
            return img, "OK"
        except subprocess.TimeoutExpired:
            return None, "截图超时"
        except Exception as e:
            return None, f"截图失败: {e}"[:100]
