"""通用麻将规则接口
注意：以下为通用测试规则，非本游戏确认规则
"""
from collections import Counter

def _can_form_melds(counts):
    """递归检查是否能分解为面子（刻子或顺子）"""
    # 找到第一张有剩余的牌
    for tile in range(34):
        if counts[tile] > 0:
            break
    else:
        return True  # 全部用完
    
    # 尝试刻子
    if counts[tile] >= 3:
        counts[tile] -= 3
        if _can_form_melds(counts):
            counts[tile] += 3
            return True
        counts[tile] += 3
    
    # 尝试顺子（仅数牌）
    suit = tile // 9
    rank = tile % 9
    if suit < 3 and rank <= 6:  # 1-7 可做顺子头
        if counts[tile+1] > 0 and counts[tile+2] > 0:
            counts[tile] -= 1
            counts[tile+1] -= 1
            counts[tile+2] -= 1
            if _can_form_melds(counts):
                counts[tile] += 1
                counts[tile+1] += 1
                counts[tile+2] += 1
                return True
            counts[tile] += 1
            counts[tile+1] += 1
            counts[tile+2] += 1
    
    return False

def is_winning_hand(tiles, rule_name="generic_4m1p"):
    """
    胡牌判断（通用 4面子+1雀头）
    :param tiles: 14 张牌编码列表
    :param rule_name: 规则名称（仅用于标识）
    :return: (bool, reason)
    """
    known = [t for t in tiles if t != -1]
    if len(known) != 14:
        return False, f"Need 14 known tiles, got {len(known)}"
    
    counts = Counter(known)
    
    # 尝试每种对子作为雀头
    for tile in range(34):
        if counts[tile] >= 2:
            counts[tile] -= 2
            if _can_form_melds(counts.copy()):
                counts[tile] += 2
                return True, f"Winning with pair {tile} (rule: {rule_name})"
            counts[tile] += 2
    
    return False, "No valid decomposition"

def get_discard_candidates(tiles):
    """生成出牌候选（结构上可移除的牌）"""
    return [i for i, t in enumerate(tiles) if t != -1]

def check_ting(tiles, rule_name="generic_4m1p"):
    """
    听牌判断：13 张牌，补哪些牌可胡
    :return: (bool, waiting_list)
    """
    known = [t for t in tiles if t != -1]
    if len(known) != 13:
        return False, []
    
    waiting = []
    for t in range(34):
        if known.count(t) < 4:
            test = known + [t]
            win, _ = is_winning_hand(test, rule_name)
            if win:
                waiting.append(t)
    
    return len(waiting) > 0, waiting
