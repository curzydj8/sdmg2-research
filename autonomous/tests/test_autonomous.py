"""自主学习模块测试"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from autonomous.observation import ObservationEngine, GameObservation
from autonomous.state_machine import GameStateMachine
from autonomous.hypothesis import RuleHypothesisEngine, RuleHypothesis, EvidenceLevel
from autonomous.planner import ActionPlanner
from autonomous.verifier import OutcomeVerifier
from autonomous.memory import ExperienceMemory, ExperienceRecord
from autonomous.doubleup import DoubleUpRuleModel
from autonomous.grandslam import GrandSlamRuleModel
from autonomous.game_rules import GameSpecificRules

def test_observation():
    eng = ObservationEngine(mode="OBSERVE_ONLY")
    # 用现有截图测试
    obs = eng.observe("screenshots/bet002-poll3.png", "test_sha")
    assert obs.state == "MAIN_GAME", f"Expected MAIN_GAME, got {obs.state}"
    print("test_observation PASSED")

def test_state_machine():
    sm = GameStateMachine()
    assert sm.is_confirmed("MAIN_GAME")
    assert sm.is_confirmed("UNKNOWN_STATE")
    assert not sm.is_confirmed("DOUBLE_UP")  # 未证实
    print("test_state_machine PASSED")

def test_hypothesis_e_level():
    eng = RuleHypothesisEngine()
    r = RuleHypothesis(
        rule_id="R-001",
        description="测试假设",
        source="测试",
        evidence_level=EvidenceLevel.E_HYPOTHESIS,
    )
    eng.add_hypothesis(r)
    assert not eng.rules["R-001"].allowed_for_decision
    print("test_hypothesis_e_level PASSED")

def test_planner_no_execute():
    planner = ActionPlanner(mode="PLAN_ONLY")
    plans = planner.plan(None, None, None)
    assert plans == []
    ok, reason = planner.check_authorization(None)
    assert not ok
    print("test_planner_no_execute PASSED")

def test_game_rules_not_implemented():
    gr = GameSpecificRules()
    result, msg = gr.is_winning_hand([])
    assert result is None
    assert "NOT_IMPLEMENTED" in msg
    print("test_game_rules_not_implemented PASSED")

def test_doubleup_predict():
    m = DoubleUpRuleModel()
    pred = m.predict("最高档位")
    assert "不允许执行" in pred or "否" in pred
    print("test_doubleup_predict PASSED")

def test_grandslam_distinguish():
    m = GrandSlamRuleModel()
    d = m.distinguish()
    assert len(d["observed_screens"]) > 0
    assert len(d["confirmed_rules"]) == 0
    assert len(d["unknown_mechanisms"]) > 0
    print("test_grandslam_distinguish PASSED")

if __name__ == "__main__":
    test_observation()
    test_state_machine()
    test_hypothesis_e_level()
    test_planner_no_execute()
    test_game_rules_not_implemented()
    test_doubleup_predict()
    test_grandslam_distinguish()
    print("\nAll autonomous tests passed!")
