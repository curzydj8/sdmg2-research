"""HumanBehaviorProfile：人类行为模型"""
from collections import Counter, defaultdict

class HumanBehaviorProfile:
    """从数据学习人类行为（样本不足时返回 INSUFFICIENT_DATA）"""
    
    def __init__(self, min_samples=10):
        self.min_samples = min_samples
        self.actions = defaultdict(list)  # state -> [actions]
    
    def record(self, state, action, evidence=""):
        self.actions[state].append((action, evidence))
    
    def get_profile(self, state):
        """获取某状态下的人类行为统计"""
        samples = self.actions.get(state, [])
        if len(samples) < self.min_samples:
            return {"status": "INSUFFICIENT_DATA", "samples": len(samples)}
        
        counter = Counter(a for a, _ in samples)
        total = len(samples)
        return {
            "status": "OK",
            "samples": total,
            "distribution": {k: v/total for k, v in counter.items()},
        }
