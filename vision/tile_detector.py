"""单牌检测"""
def detect_tiles(hand_img, expected_count=14):
    """
    从手牌区域图像中分割单张牌
    :return: list of {"index", "bbox", "crop"}
    """
    w, h = hand_img.size
    tile_w = w // expected_count
    tiles = []
    for i in range(expected_count):
        x = i * tile_w
        # 最后一张可能有余数，调整
        tw = tile_w if i < expected_count - 1 else w - x
        tiles.append({
            "index": i + 1,
            "bbox": [x, 0, tw, h],
            "width": tw,
            "height": h
        })
    return tiles
