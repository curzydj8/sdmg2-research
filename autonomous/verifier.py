"""OutcomeVerifier：结果验证器"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class VerificationResult:
    observed: bool
    matches_prediction: Optional[bool] = None
    state_changed: bool = False
    credit_changed: bool = False
    credit_before: Optional[int] = None
    credit_after: Optional[int] = None
    causal_evidence: str = "insufficient"  # sufficient/insufficient

class OutcomeVerifier:
    """结果验证器"""
    
    def verify(self, before, after, prediction) -> VerificationResult:
        """对比动作前后观察"""
        return VerificationResult(
            observed=True,
            matches_prediction=None,  # 需具体比较
            state_changed=before.state != after.state,
            credit_changed=before.credit != after.credit,
            credit_before=before.credit,
            credit_after=after.credit,
            causal_evidence="insufficient",  # 一次成功不能证明因果
        )
