"""牌面编码"""
# 内部编码：0-33
# 0-8: 1m-9m (万)
# 9-17: 1p-9p (筒)
# 18-26: 1s-9s (索)
# 27-30: E,S,W,N (风)
# 31-33: Wh,G,R (三元)

TILE_NAMES = (
    [f"{i+1}m" for i in range(9)] +
    [f"{i+1}p" for i in range(9)] +
    [f"{i+1}s" for i in range(9)] +
    ["E", "S", "W", "N", "Wh", "G", "R"]
)

def encode(tile_str):
    """牌面字符串转编码"""
    if tile_str == "UNKNOWN_TILE":
        return -1
    try:
        return TILE_NAMES.index(tile_str)
    except ValueError:
        raise ValueError(f"Invalid tile: {tile_str}")

def decode(code):
    """编码转牌面字符串"""
    if code == -1:
        return "UNKNOWN_TILE"
    if 0 <= code < 34:
        return TILE_NAMES[code]
    raise ValueError(f"Invalid code: {code}")

def is_valid_code(code):
    """检查编码是否合法"""
    return code == -1 or (0 <= code < 34)
