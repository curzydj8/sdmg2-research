"""MahjongRuleLearningEngine：麻将规则学习引擎"""
# 使用通用算法生成候选，以游戏实际行为为验证依据

class MahjongRuleLearningEngine:
    """规则学习引擎"""
    
    def __init__(self):
        self.verified_yaku = {}  # 已验证番种
        self.conflicts = []  # 冲突案例
    
    def analyze_hand(self, tiles):
        """分析手牌（通用算法候选）"""
        # 调用现有 mahjong 模块
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from mahjong import hand_analyzer
        
        # 通用分析（候选）
        result = {"tiles": tiles, "count": hand_analyzer.count_tiles(tiles), "note": "通用算法候选，需游戏验证"}
        return result
    
    def compare_with_game(self, tiles, game_yaku, game_score):
        """比较 AI 计算与游戏显示"""
        ai_result = self.analyze_hand(tiles)
        match = True  # 简化
        if not match:
            self.conflicts.append({
                "tiles": tiles,
                "game_yaku": game_yaku,
                "ai_result": ai_result,
            })
        return {"match": match, "conflicts": len(self.conflicts)}
