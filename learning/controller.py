"""AutonomousLearningController：自主学习控制器"""
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
import uuid

@dataclass
class UnknownQuestion:
    """未知问题"""
    qid: str
    description: str
    importance: str
    known_evidence: List[str] = field(default_factory=list)
    hypotheses: List[str] = field(default_factory=list)
    required_action: str = ""
    risk: str = ""
    needs_auth: bool = False
    success_criteria: str = ""
    conclusion: str = ""
    confidence: str = "UNKNOWN"
    next_task: str = ""


# DIP 模式知识（2026-10-14 实测）
DIP_CONTROLS = {
    "Mahjong": {"value": 0x40, "bet_via_button2": False, "default": True},
    "Joystick": {"value": 0x00, "bet_via_button2": True, "default": False},
}
# Bet (IPT_BUTTON2) 仅在 Joystick 模式有效
# Credit Limit = 2000（积分上限，非比倍上限）

class AutonomousLearningController:
    """自主学习控制器"""
    
    def __init__(self):
        self.questions = {}
        self._init_questions()
    
    def _init_questions(self):
        """初始化未知问题（AI 自主发现）"""
        questions = [
            ("Q-001", "下注操作的真实按键映射是什么？", "高：阻塞主对局"),
            ("Q-002", "BET 的单位和合法范围是什么？", "高：阻塞下注"),
            ("Q-003", "如何进入主对局可玩状态？", "高：阻塞实战"),
            ("Q-004", "比倍的进入条件是什么？", "中：核心玩法"),
            ("Q-005", "半比和全比的区别是什么？", "中：比倍玩法"),
            ("Q-006", "大满贯的触发条件是什么？", "中：高级玩法"),
            ("Q-007", "CREDIT 与游戏分数的换算关系？", "高：基础"),
            ("Q-008", "比倍爆机时 6 与 W 的区别？", "低：显示问题"),
            ("Q-009", "游戏设置菜单入口在哪？", "中：配置"),
            ("Q-010", "吃碰杠听胡的操作方式？", "高：主对局"),
        ]
        for qid, desc, imp in questions:
            self.questions[qid] = UnknownQuestion(
                qid=qid, description=desc, importance=imp,
            )
    
    def get_prioritized(self) -> List[UnknownQuestion]:
        """按重要性排序"""
        priority = {"高": 0, "中": 1, "低": 2}
        return sorted(self.questions.values(),
                     key=lambda q: priority.get(q.importance[0], 3))
    
    def update(self, qid, conclusion, confidence):
        """更新问题结论"""
        if qid in self.questions:
            self.questions[qid].conclusion = conclusion
            self.questions[qid].confidence = confidence
