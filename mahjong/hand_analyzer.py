"""手牌分析器"""
from .tile import decode
from collections import Counter

def count_tiles(tiles):
    """统计牌数"""
    c = Counter(t for t in tiles if t != -1)
    return dict(c)

def hand_to_str(tiles):
    """手牌转字符串"""
    return " ".join(decode(t) for t in tiles)
