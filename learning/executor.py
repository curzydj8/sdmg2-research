"""GameActionExecutor：游戏动作执行器"""
import yaml
import os

class GameActionExecutor:
    """动作执行器（读取策略配置）"""
    
    def __init__(self, policy_path="config/autonomy_policy.yaml"):
        with open(policy_path) as f:
            self.policy = yaml.safe_load(f)
        self.protected_pid = self.policy["hard_boundaries"]["protected_pid"]
    
    def check_isolation(self, target_pid):
        """检查隔离"""
        if target_pid == self.protected_pid:
            return (False, "目标是受保护的原始实例")
        return (True, "隔离检查通过")
    
    def is_authorized(self, action_type):
        """检查授权"""
        authorized = self.policy.get("authorized", [])
        # 普通游戏操作在授权范围内
        if action_type in ["observe", "analyze", "simulate"]:
            return True
        if action_type == "game_action":
            return "隔离实例中的普通游戏操作" in str(authorized)
        return False
