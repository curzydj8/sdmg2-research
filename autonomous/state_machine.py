"""GameStateMachine：游戏状态机"""
from dataclasses import dataclass, field
from typing import List, Optional

# 候选状态（不代表已证实存在）
CANDIDATE_STATES = [
    "UNKNOWN_STATE",
    "TITLE",
    "MAIN_GAME",
    "BET_SELECTION",
    "PLAYING",
    "RESULT",
    "ODDS",
    "DOUBLE_UP",
    "REWARD",
    "GRAND_SLAM",
    "PAUSED",
    "ERROR",
]

@dataclass
class StateDefinition:
    """状态定义"""
    name: str
    entry_conditions: List[str] = field(default_factory=list)
    observable_evidence: List[str] = field(default_factory=list)
    possible_prev: List[str] = field(default_factory=list)
    possible_next: List[str] = field(default_factory=list)
    confidence: float = 0.0
    allowed_actions: List[str] = field(default_factory=list)
    forbidden_actions: List[str] = field(default_factory=list)
    confirmed: bool = False  # 是否已证实存在

class GameStateMachine:
    """游戏状态机"""
    
    def __init__(self):
        self.states = {}
        self._init_states()
    
    def _init_states(self):
        # UNKNOWN_STATE：默认
        self.states["UNKNOWN_STATE"] = StateDefinition(
            name="UNKNOWN_STATE",
            observable_evidence=["无法识别"],
            allowed_actions=[],
            forbidden_actions=["所有游戏操作"],
            confirmed=True,
        )
        # MAIN_GAME：已证实（画面证据）
        self.states["MAIN_GAME"] = StateDefinition(
            name="MAIN_GAME",
            entry_conditions=["底部出现 14 张牌"],
            observable_evidence=["底部浅色牌区"],
            possible_next=["REWARD", "ODDS", "UNKNOWN_STATE"],
            allowed_actions=["观察"],
            forbidden_actions=["自动按键（当前阶段）"],
            confirmed=True,
        )
        # 其他：未证实，标记为假设
        for s in ["TITLE", "BET_SELECTION", "PLAYING", "RESULT", "ODDS",
                  "DOUBLE_UP", "REWARD", "GRAND_SLAM", "PAUSED", "ERROR"]:
            confirmed = s in ["REWARD", "ODDS", "TITLE"]  # 有截图证据
            self.states[s] = StateDefinition(
                name=s,
                observable_evidence=[f"{s} 画面特征待确认"],
                allowed_actions=["观察"],
                forbidden_actions=["自动按键（当前阶段）"],
                confirmed=confirmed,
            )
    
    def get_state(self, name) -> Optional[StateDefinition]:
        return self.states.get(name)
    
    def is_confirmed(self, name) -> bool:
        s = self.states.get(name)
        return s.confirmed if s else False
