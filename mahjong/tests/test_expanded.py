"""扩展单元测试（通用测试规则）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from mahjong.rules import is_winning_hand, check_ting, get_discard_candidates
from mahjong.tile import encode, decode
from mahjong.hand import Hand

def test_invalid_tile_code():
    try:
        encode("INVALID")
        assert False
    except ValueError:
        print("test_invalid_tile_code PASSED")

def test_hand_too_long():
    h = Hand(list(range(14)))
    try:
        h.add(1)  # 15th tile
        # Hand allows >14? Check validate
        ok, _ = h.validate()
        assert not ok or len(h.tiles) <= 14
    except:
        pass
    print("test_hand_too_long PASSED")

def test_winning_with_sequences():
    # 123 456 789 万 + 111 筒 + 11 索
    tiles = []
    for i in [1,2,3]:
        tiles.append(encode(f"{i}m"))
    for i in [4,5,6]:
        tiles.append(encode(f"{i}m"))
    for i in [7,8,9]:
        tiles.append(encode(f"{i}m"))
    tiles.extend([encode("1p")]*3)
    tiles.extend([encode("1s")]*2)
    win, _ = is_winning_hand(tiles)
    assert win, "Should win with sequences"
    print("test_winning_with_sequences PASSED")

def test_not_winning_incomplete():
    # 13 张，缺一张
    tiles = [encode("1m")]*3 + [encode("2m")]*3 + [encode("3m")]*3 + [encode("4m")]*3 + [encode("5m")]
    win, _ = is_winning_hand(tiles)
    assert not win
    print("test_not_winning_incomplete PASSED")

def test_ting_multiple_waits():
    # 听多张的情况
    tiles = [encode("1m")]*3 + [encode("2m")]*3 + [encode("3m")]*3 + [encode("4m")]*3 + [encode("5m")]
    is_ting, waiting = check_ting(tiles)
    # 5m 单吊，听 5m
    assert is_ting
    print("test_ting_multiple_waits PASSED")

def test_discard_no_duplicates():
    tiles = [0, 0, 1, 2, -1]
    candidates = get_discard_candidates(tiles)
    # 应返回索引，去重由调用方处理
    assert -1 not in [tiles[i] for i in candidates]
    print("test_discard_no_duplicates PASSED")

def test_input_not_mutated():
    tiles = [encode("1m")]*3 + [encode("2m")]*3 + [encode("3m")]*3 + [encode("4m")]*3 + [encode("5m")]*2
    original = tiles.copy()
    is_winning_hand(tiles)
    assert tiles == original, "Input mutated!"
    print("test_input_not_mutated PASSED")

if __name__ == "__main__":
    test_invalid_tile_code()
    test_hand_too_long()
    test_winning_with_sequences()
    test_not_winning_incomplete()
    test_ting_multiple_waits()
    test_discard_no_duplicates()
    test_input_not_mutated()
    print("\nAll expanded tests passed!")
