"""规则算法单元测试（使用通用测试规则）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from mahjong.rules import is_winning_hand, check_ting, get_discard_candidates
from mahjong.tile import encode

def test_winning_simple():
    # 111 222 333 444 55 (万)
    tiles = [encode(f"{i}m")*3 for i in [1,2,3,4]] + [encode("5m")]*2
    tiles = [t for sub in [[encode(f"{i}m")]*3 for i in [1,2,3,4]] for t in sub] + [encode("5m")]*2
    win, reason = is_winning_hand(tiles)
    assert win, f"Should win: {reason}"
    print("test_winning_simple PASSED")

def test_not_winning():
    # 杂牌
    tiles = [encode("1m"), encode("2m"), encode("3m"), encode("4m"),
             encode("5m"), encode("6m"), encode("7m"), encode("8m"),
             encode("9m"), encode("1p"), encode("2p"), encode("3p"),
             encode("4p"), encode("5p")]
    win, _ = is_winning_hand(tiles)
    assert not win
    print("test_not_winning PASSED")

def test_ting():
    # 听牌：111 222 333 444 5 (等 5m)
    tiles = []
    for i in [1,2,3,4]:
        tiles.extend([encode(f"{i}m")]*3)
    tiles.append(encode("5m"))
    is_ting, waiting = check_ting(tiles)
    assert is_ting
    assert encode("5m") in waiting
    print("test_ting PASSED")

def test_discard_candidates():
    tiles = [0, 1, 2, -1, 4]  # 含 UNKNOWN
    candidates = get_discard_candidates(tiles)
    assert candidates == [0, 1, 2, 4]  # 排除 UNKNOWN
    print("test_discard_candidates PASSED")

if __name__ == "__main__":
    test_winning_simple()
    test_not_winning()
    test_ting()
    test_discard_candidates()
    print("\nAll rule tests passed!")
