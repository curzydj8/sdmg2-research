"""GameSpecificRules：游戏专属规则接口"""
# 未来确认的《超级大满贯Ⅱ》规则通过此接口接入
# 未实现时返回 NOT_IMPLEMENTED，不得回退到通用规则

class GameSpecificRules:
    """游戏专属规则（当前全部未实现）"""
    
    def is_winning_hand(self, tiles):
        return (None, "NOT_IMPLEMENTED: 本游戏胡牌规则未确认")
    
    def check_ting(self, tiles):
        return (None, "NOT_IMPLEMENTED: 本游戏听牌规则未确认")
    
    def get_legal_discards(self, tiles):
        return (None, "NOT_IMPLEMENTED: 本游戏出牌规则未确认")
