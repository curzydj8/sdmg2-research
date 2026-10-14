#!/usr/bin/env python3
"""
打牌策略 v1.0
基于已验证的牌型理解（超級大滿貫II 2人麻将）
"""
class MahjongStrategy:
    """
    策略优先级（从先打到后打）：
    1. 孤张字牌（东南西北、中发白，无对子搭子）
    2. 孤张边牌（1、9，无搭子）
    3. 孤张中张（2-8，无搭子）
    4. 有搭子的牌（保留）
    
    注意：此为通用麻将启发式，未针对本游戏特殊规则调优。
    """
    
    HONORS = set(["东", "南", "西", "北", "中", "发", "白"])
    TERMINALS = set(["1万","1筒","1条","9万","9筒","9条"])
    
    def choose_discard(self, hand):
        """
        :param hand: [(slot, tile_name, confidence), ...]，如 [('a','四万',1.0), ...]
        :return: (slot, reason) 或 (None, "无法决策")
        """
        # 只考虑高置信度牌
        known = [(s,t) for s,t,c in hand if c >= 0.8 and t != "UNKNOWN"]
        if not known:
            return None, "无高置信度牌面，不决策"
        
        # 统计每种牌的数量
        from collections import Counter
        counts = Counter(t for _,t in known)
        
        # 1. 孤张字牌
        for slot, tile in known:
            if tile in self.HONORS and counts[tile] == 1:
                return slot, f"孤张字牌 {tile}"
        
        # 2. 孤张边牌
        for slot, tile in known:
            if tile in self.TERMINALS and counts[tile] == 1:
                return slot, f"孤张边牌 {tile}"
        
        # 3. 孤张中张（简单：数量为1的非字牌）
        for slot, tile in known:
            if tile not in self.HONORS and counts[tile] == 1:
                return slot, f"孤张 {tile}"
        
        # 4. 实在没有孤张，打第一张（需人工确认）
        return known[0][0], f"无孤张，默认打 {known[0][1]}（需确认）"
