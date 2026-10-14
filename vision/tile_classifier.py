"""牌面分类器（基础版）"""
def classify_tile(tile_img):
    """
    识别单张牌面
    当前为占位实现，返回 UNKNOWN
    :return: {"label", "confidence", "needs_review"}
    """
    # TODO: 实现模板匹配或特征分类
    return {
        "predicted_label": "UNKNOWN_TILE",
        "confidence": 0.0,
        "alternatives": [],
        "needs_review": True
    }
