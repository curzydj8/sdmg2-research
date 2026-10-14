"""高质量测试：数据契约与内部一致性"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from mahjong.tile import encode, decode, TILE_NAMES
from mahjong.rules import is_winning_hand, check_ting, get_discard_candidates
from mahjong.hand import Hand

def test_encode_decode_roundtrip():
    """编码解码往返一致性"""
    for i, name in enumerate(TILE_NAMES):
        assert decode(encode(name)) == name, f"Failed for {name}"
        assert encode(decode(i)) == i
    assert decode(encode("UNKNOWN_TILE")) == "UNKNOWN_TILE"
    print("test_encode_decode_roundtrip PASSED")

def test_boundary_values():
    """边界值"""
    # 合法边界
    assert decode(0) == "1m"
    assert decode(33) == "R"
    # 非法
    try:
        decode(34)
        assert False
    except ValueError:
        pass
    try:
        decode(-2)
        assert False
    except ValueError:
        pass
    print("test_boundary_values PASSED")

def test_ting_candidates_valid():
    """听牌候选必须真实可胡"""
    # 13 张听牌型
    tiles = [encode("1m")]*3 + [encode("2m")]*3 + [encode("3m")]*3 + [encode("4m")]*3 + [encode("5m")]
    is_ting, waiting = check_ting(tiles)
    assert is_ting
    for w in waiting:
        test_hand = tiles + [w]
        win, _ = is_winning_hand(test_hand)
        assert win, f"Waiting tile {w} should win"
    print("test_ting_candidates_valid PASSED")

def test_discard_from_hand():
    """出牌候选必须来自手牌"""
    tiles = [encode("1m"), encode("2m"), encode("3m")]
    candidates = get_discard_candidates(tiles)
    for idx in candidates:
        assert 0 <= idx < len(tiles), "Index out of range"
        assert tiles[idx] != -1, "Should not include UNKNOWN"
    print("test_discard_from_hand PASSED")

def test_determinism():
    """同一输入重复分析结果一致"""
    tiles = [encode("1m")]*3 + [encode("2m")]*3 + [encode("3m")]*3 + [encode("4m")]*3 + [encode("5m")]*2
    r1 = is_winning_hand(tiles)
    r2 = is_winning_hand(tiles)
    assert r1 == r2, "Non-deterministic!"
    print("test_determinism PASSED")

def test_random_stability():
    """随机合法输入稳定性（固定种子）"""
    random.seed(42)
    for _ in range(20):
        # 生成随机 14 张（每种最多 4 张）
        counts = [0]*34
        tiles = []
        while len(tiles) < 14:
            t = random.randint(0, 33)
            if counts[t] < 4:
                counts[t] += 1
                tiles.append(t)
        # 不应崩溃
        win, reason = is_winning_hand(tiles)
        assert isinstance(win, bool)
        assert isinstance(reason, str)
    print("test_random_stability PASSED (seed=42, n=20)")

def test_empty_input():
    """空输入处理"""
    win, reason = is_winning_hand([])
    assert not win
    print("test_empty_input PASSED")

if __name__ == "__main__":
    test_encode_decode_roundtrip()
    test_boundary_values()
    test_ting_candidates_valid()
    test_discard_from_hand()
    test_determinism()
    test_random_stability()
    test_empty_input()
    print("\nAll quality tests passed!")
