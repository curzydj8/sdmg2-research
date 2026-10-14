"""置信度计算"""
def calculate_overall_confidence(state_conf, tile_confs):
    """计算整体置信度"""
    if not tile_confs:
        return state_conf * 0.5
    avg_tile = sum(tile_confs) / len(tile_confs)
    return (state_conf + avg_tile) / 2
