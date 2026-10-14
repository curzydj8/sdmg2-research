"""ActionPlanner：动作规划器（只规划，不执行）"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ActionCandidate:
    """候选动作"""
    goal: str
    applicable_state: str
    expected_result: str
    side_effects: List[str] = field(default_factory=list)
    evidence: str = ""
    preconditions: List[str] = field(default_factory=list)
    stop_conditions: List[str] = field(default_factory=list)
    # 当前阶段：不执行
    executable: bool = False

class ActionPlanner:
    """动作规划器"""
    
    def __init__(self, mode="PLAN_ONLY"):
        assert mode in ["OBSERVE_ONLY", "ANALYZE", "SIMULATE", "PLAN_ONLY"]
        self.mode = mode
    
    def plan(self, observation, state_machine, hypothesis_engine) -> List[ActionCandidate]:
        """生成候选动作（不执行）"""
        # 当前阶段：返回空计划，仅演示接口
        return []
    
    def check_authorization(self, action: ActionCandidate) -> tuple:
        """授权检查"""
        # 当前阶段：所有游戏操作均未授权
        return (False, "当前阶段禁止执行游戏动作")
