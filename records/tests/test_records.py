"""记录系统测试（合成数据）"""
import sys, os, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from records.schema import init_db
from records.ledger import CreditLedger
from records.pnl import PnLStats
from records.behavior import HumanBehaviorProfile
from records.simulator import GameSimulator
import sqlite3

def test_ledger():
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db = f.name
    init_db(db)
    ledger = CreditLedger(db)
    
    # 合成数据：一局，上分 1000，下注 10，返还 0
    ledger.record("g1", 1000, "TOP_UP", 1000, "合成测试")
    ledger.record("g1", -10, "BET", 990, "合成测试")
    
    ok, msg = ledger.verify("g1", 0)
    assert ok, msg
    assert ledger.get_balance("g1") == 990
    print("test_ledger PASSED")
    os.unlink(db)

def test_pnl():
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db = f.name
    init_db(db)
    conn = sqlite3.connect(db)
    # 合成 3 局：1 胜，1 负，1 平
    conn.execute("INSERT INTO game_rounds VALUES ('g1','s1','t','t',1000,1010,10,'WIN',1)")
    conn.execute("INSERT INTO game_rounds VALUES ('g2','s1','t','t',1010,1000,10,'LOSS',1)")
    conn.execute("INSERT INTO game_rounds VALUES ('g3','s1','t','t',1000,1000,10,'DRAW',1)")
    conn.execute("INSERT INTO credit_ledger VALUES ('e1','g1','t',1000,'TOP_UP',1000,'')")
    conn.execute("INSERT INTO credit_ledger VALUES ('e2','g1','t',-10,'BET',990,'')")
    conn.execute("INSERT INTO credit_ledger VALUES ('e3','g1','t',20,'WIN_RETURN',1010,'')")
    conn.commit()
    conn.close()
    
    stats = PnLStats(db).compute()
    assert stats["settled_rounds"] == 3
    assert stats["wins"] == 1
    assert stats["losses"] == 1
    print("test_pnl PASSED (synthetic data)")
    os.unlink(db)

def test_behavior_insufficient():
    bp = HumanBehaviorProfile(min_samples=10)
    bp.record("ODDS", "BET_MAX", "合成")
    result = bp.get_profile("ODDS")
    assert result["status"] == "INSUFFICIENT_DATA"
    print("test_behavior_insufficient PASSED")

def test_simulator_marked():
    sim = GameSimulator(seed=42)
    result = sim.simulate_round(1000, 10)
    assert result["is_simulation"] == True
    assert result["status"] == "UNKNOWN_RULE"
    print("test_simulator_marked PASSED")

if __name__ == "__main__":
    test_ledger()
    test_pnl()
    test_behavior_insufficient()
    test_simulator_marked()
    print("\nAll record tests passed! (synthetic data)")
