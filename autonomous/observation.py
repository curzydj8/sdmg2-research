"""ObservationEngine：游戏观察引擎"""
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class GameObservation:
    """统一观察数据结构"""
    timestamp: str
    screenshot_path: str
    screenshot_sha256: str
    state: str  # 游戏状态，UNKNOWN_STATE 如果无法识别
    state_confidence: float
    state_evidence: list = field(default_factory=list)
    credit: Optional[int] = None
    bet: Optional[int] = None
    odds_visible: bool = False
    raw_data: Dict[str, Any] = field(default_factory=dict)

class ObservationEngine:
    """观察引擎：只读取，不操作"""
    
    def __init__(self, mode="OBSERVE_ONLY"):
        assert mode in ["OBSERVE_ONLY", "ANALYZE", "SIMULATE", "PLAN_ONLY"], \
            f"Mode {mode} not allowed in current phase"
        self.mode = mode
    
    def observe(self, screenshot_path, screenshot_sha256=""):
        """从截图生成观察记录"""
        # 使用现有 vision 模块
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from vision.state_classifier import classify_state
        
        result = classify_state(screenshot_path)
        
        return GameObservation(
            timestamp=datetime.now().isoformat(),
            screenshot_path=screenshot_path,
            screenshot_sha256=screenshot_sha256,
            state=result["state"],
            state_confidence=result["confidence"],
            state_evidence=result.get("evidence", []),
            raw_data={"classifier_reason": result.get("reason", "")}
        )
