"""RuleHypothesisEngine：规则假设引擎"""
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class EvidenceLevel(Enum):
    A_OFFICIAL = "A"  # 官方说明
    B_SOURCE = "B"    # MAME 源码事实
    C_OBSERVED = "C"  # 直接观察
    D_INFERRED = "D"  # 多次实验推断
    E_HYPOTHESIS = "E"  # 未验证假设

@dataclass
class RuleHypothesis:
    """规则假设"""
    rule_id: str
    description: str
    source: str
    evidence_level: EvidenceLevel
    evidence: List[str] = field(default_factory=list)
    support_count: int = 0
    counterexamples: List[str] = field(default_factory=list)
    verified: bool = False
    allowed_for_decision: bool = False  # E 级不允许

class RuleHypothesisEngine:
    """规则假设引擎"""
    
    def __init__(self):
        self.rules = {}
    
    def add_hypothesis(self, rule: RuleHypothesis):
        # E 级假设不允许用于决策
        if rule.evidence_level == EvidenceLevel.E_HYPOTHESIS:
            rule.allowed_for_decision = False
        self.rules[rule.rule_id] = rule
    
    def get_verified_rules(self):
        return {k: v for k, v in self.rules.items() if v.verified}
    
    def explain(self, rule_id) -> str:
        """解释规则判断的证据来源"""
        r = self.rules.get(rule_id)
        if not r:
            return f"规则 {rule_id} 未知"
        return (f"规则 {rule_id}: {r.description}\n"
                f"证据等级: {r.evidence_level.value}\n"
                f"来源: {r.source}\n"
                f"支持次数: {r.support_count}\n"
                f"已验证: {r.verified}\n"
                f"允许决策: {r.allowed_for_decision}")
