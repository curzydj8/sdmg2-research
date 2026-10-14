"""内部模拟器（与真实游戏隔离）"""
import random

class GameSimulator:
    """内部模拟器：未知规则返回 UNKNOWN_RULE"""
    
    def __init__(self, seed=42):
        self.seed = seed
        random.seed(seed)
        self.model_version = "0.1.0"
    
    def simulate_round(self, initial_credit, bet_amount, strategy="default"):
        """
        模拟一局
        注意：真实规则未知，此为占位实现
        """
        return {
            "status": "UNKNOWN_RULE",
            "message": "游戏专属规则未实现，无法模拟",
            "model_version": self.model_version,
            "seed": self.seed,
            "is_simulation": True,  # 明确标记非真实记录
        }
