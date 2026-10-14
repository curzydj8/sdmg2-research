"""手牌区域检测"""
def detect_hand_region(img):
    """
    检测手牌区域
    基于相对坐标（适应不同分辨率）
    :return: (x, y, w, h, confidence)
    """
    w, h = img.size
    # 手牌在底部：x=3%-97%, y=79%-95%
    x = int(w * 0.03)
    y = int(h * 0.79)
    rw = int(w * 0.94)
    rh = int(h * 0.16)
    return {
        "bbox": [x, y, rw, rh],
        "confidence": 0.8,
        "method": "relative_coords"
    }
