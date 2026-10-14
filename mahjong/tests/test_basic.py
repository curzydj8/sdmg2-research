"""基础单元测试"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from mahjong.tile import encode, decode, is_valid_code
from mahjong.hand import Hand

def test_encode_decode():
    assert encode("1m") == 0
    assert encode("9s") == 26
    assert encode("R") == 33
    assert decode(0) == "1m"
    assert decode(33) == "R"
    assert encode("UNKNOWN_TILE") == -1
    print("test_encode_decode PASSED")

def test_hand_valid():
    h = Hand([0, 0, 0, 1, 2, 3])
    ok, msg = h.validate()
    assert ok, msg
    print("test_hand_valid PASSED")

def test_hand_too_many():
    h = Hand([0]*4 + [1]*4 + [2]*4 + [3]*3)  # 15 张
    ok, msg = h.validate()
    assert not ok
    print("test_hand_too_many PASSED")

def test_hand_duplicate_exceed():
    try:
        h = Hand([0]*5)  # 5 张同一牌
        assert False, "Should raise"
    except ValueError:
        print("test_hand_duplicate_exceed PASSED")

if __name__ == "__main__":
    test_encode_decode()
    test_hand_valid()
    test_hand_too_many()
    test_hand_duplicate_exceed()
    print("\nAll tests passed!")
