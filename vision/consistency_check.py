"""一致性检查"""
def check_consistency(detection_result, img_size):
    """检查检测结果一致性"""
    issues = []
    w, h = img_size
    
    # 1. 检查框是否超出边界
    for tile in detection_result.get("tiles", []):
        x, y, tw, th = tile["bbox"]
        if x < 0 or y < 0 or x+tw > w or y+th > h:
            issues.append(f"Tile {tile['index']} out of bounds")
    
    # 2. 检查牌数
    tile_count = len(detection_result.get("tiles", []))
    if tile_count != 14:
        issues.append(f"Tile count is {tile_count}, expected 14")
    
    # 3. 检查重叠（简化）
    # TODO: 实现重叠检测
    
    return {
        "passed": len(issues) == 0,
        "issues": issues,
        "tile_count": tile_count
    }
