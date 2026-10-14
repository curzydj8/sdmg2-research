"""游戏状态分类器（阶段二十六修订版）
区分：DEMO_OR_ATTRACT, WINNING_HAND_DISPLAY, MAIN_GAME_CANDIDATE, 等
"""
from PIL import Image

# 候选状态
STATES = [
    "DEMO_OR_ATTRACT",
    "WINNING_HAND_DISPLAY",
    "MAIN_GAME_CANDIDATE",
    "CREDIT_ENTRY_OR_SETUP",
    "ODDS",
    "DOUBLE_UP",
    "GRAND_SLAM",
    "REWARD",
    "TITLE",
    "PAUSED",
    "UNKNOWN_STATE",
]

def _bottom_light_ratio(img):
    w, h = img.size
    bottom = img.crop((0, int(h*0.75), w, h))
    pixels = list(bottom.getdata())
    return sum(1 for r,g,b in pixels if r>180 and g>180 and b>180) / len(pixels)

def _top_text_density(img):
    """顶部文字密度（胡牌展示有大字）"""
    w, h = img.size
    top = img.crop((0, 0, w, int(h*0.3)))
    # 转换为灰度，计算边缘密度（简化）
    gray = top.convert('L')
    pixels = list(gray.getdata())
    # 大文字区域通常有高对比度
    mean = sum(pixels) / len(pixels)
    var = sum((p-mean)**2 for p in pixels) / len(pixels)
    return var ** 0.5

def classify_state(img_path):
    from .capture_loader import load_screenshot
    try:
        img = load_screenshot(img_path)
    except:
        return {"state": "UNKNOWN_STATE", "confidence": 0.0,
                "reason": "load_failed", "evidence": [], "needs_review": True}
    
    w, h = img.size
    if w < 100 or h < 100:
        return {"state": "UNKNOWN_STATE", "confidence": 0.0,
                "reason": "too_small", "evidence": [], "needs_review": True}
    
    light_ratio = _bottom_light_ratio(img)
    text_density = _top_text_density(img)
    
    # WINNING_HAND_DISPLAY：底部有牌 + 顶部大字（如四暗刻）
    # 大字导致顶部区域方差高
    if light_ratio > 0.15 and text_density > 80:
        return {
            "state": "WINNING_HAND_DISPLAY",
            "confidence": 0.6,
            "reason": f"tiles+large_text (light={light_ratio:.2f}, text_var={text_density:.1f})",
            "evidence": ["bottom_tiles", "top_large_text"],
            "needs_review": True,
        }
    
    # MAIN_GAME_CANDIDATE：底部有牌，但无大字
    # 注意：这只是候选，不等于可操作
    if light_ratio > 0.15:
        return {
            "state": "MAIN_GAME_CANDIDATE",
            "confidence": 0.6,
            "reason": f"bottom_light_ratio={light_ratio:.2f}",
            "evidence": ["bottom_tiles"],
            "needs_review": True,
        }
    
    return {
        "state": "UNKNOWN_STATE",
        "confidence": 0.0,
        "reason": "insufficient_features",
        "evidence": [],
        "needs_review": True,
    }

def is_actionable_state(classification, credit=None, bet=None):
    """
    可玩状态门禁
    只有同时满足所有条件才返回 True
    """
    state = classification.get("state")
    
    # 条件1：状态已确认（非候选、非未知）
    if state in ["UNKNOWN_STATE", "MAIN_GAME_CANDIDATE", "DEMO_OR_ATTRACT",
                 "WINNING_HAND_DISPLAY", "REWARD", "PAUSED"]:
        return (False, f"状态 {state} 不可操作")
    
    # 条件2：CREDIT 已读取且 >0（未上分禁止）
    if credit is None or credit <= 0:
        return (False, f"CREDIT 未确认或为 0 (credit={credit})")
    
    # 条件3：明确的可操作证据
    # 当前：无已验证的可操作状态
    return (False, "暂无已验证的可操作状态")
