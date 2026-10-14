#!/usr/bin/env python3
"""
状态识别模块 v1.0
基于 states/recognition-rules.md v2.0
"""
from PIL import Image
import os

class StateDetector:
    """游戏状态识别器"""
    
    # 状态定义
    ODDS = "ODDS"           # 赔率表
    GAMEPLAY = "GAMEPLAY"   # 对局中
    UNKNOWN = "UNKNOWN"     # 未知
    
    def __init__(self, template_dir=None):
        self.template_dir = template_dir or os.path.expanduser("~/workspace/sdmg2-test/screenshots")
    
    def detect(self, img):
        """
        识别游戏状态
        :param img: PIL Image (1003x731 MAME窗口截图)
        :return: (state_id, confidence, details)
        """
        # S1: 检查 ODDS
        odds_conf = self._check_odds(img)
        if odds_conf > 0.85:
            return (self.ODDS, odds_conf, "ODDS标题匹配")
        
        # S3: 检查对局 (A-N标记)
        game_conf = self._check_gameplay(img)
        if game_conf > 0.70:
            return (self.GAMEPLAY, game_conf, "检测到手牌标记")
        
        return (self.UNKNOWN, 0.0, "无匹配状态")
    
    def _check_odds(self, img):
        """检查是否为赔率表：蓝色背景 + 顶部ODDS区域特征"""
        # 简化版：检查顶部中央区域的粉色/青色像素（ODDS标题颜色）
        # ODDS标题约在 y=50-120, x=200-800
        w, h = img.size
        crop = img.crop((int(w*0.2), int(h*0.07), int(w*0.8), int(h*0.16)))
        pixels = list(crop.getdata())
        # 粉色 (255,100,200附近) 和青色 (100,255,255附近)
        pink_cyan = sum(1 for r,g,b in pixels 
                       if (r>200 and g<150 and b>150) or (r<150 and g>200 and b>200))
        ratio = pink_cyan / len(pixels)
        # 标题区域粉/青像素占比高则为ODDS
        return min(ratio * 5, 1.0)  # 归一化
    
    def _check_gameplay(self, img):
        """检查是否为对局：底部A-N字母标记"""
        # 简化版：检查底部是否有等距的白色字母标记
        # 实际实现需OCR，此处为占位
        # 返回0表示未实现自动检测
        return 0.0  # TODO: 实现A-N检测

class MahjongVision:
    """麻将牌面识别（占位，未实现自动识别）"""
    
    def __init__(self):
        self.implemented = False
    
    def recognize_hand(self, img):
        """
        识别手牌
        :return: [(位置, 牌面, 置信度), ...]，未实现时返回空
        """
        # TODO: 实现牌面识别
        # 当前：返回空，调用者需人工确认
        return []
    
    def get_confidence(self):
        return 0.0

if __name__ == "__main__":
    print("StateDetector v1.0")
    print("ODDS检测: 基于颜色启发式")
    print("对局检测: 未实现 (需A-N OCR)")
    print("牌面识别: 未实现 (需人工)")
