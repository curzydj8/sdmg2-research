#!/usr/bin/env python3
"""
自动打牌入口 v1.0
用法: python3 run_auto_play.py [--max-actions N]
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/sdmg2-test/modules"))
from input_adapter import InputAdapter
from screen_reader import ScreenReader
from state_detector import StateDetector, MahjongVision
from mahjong_strategy import MahjongStrategy
from action_executor import ActionExecutor
from recovery_manager import RecoveryManager
from game_controller import GameController

def main():
    max_actions = 20
    for a in sys.argv[1:]:
        if a.startswith("--max-actions"):
            max_actions = int(a.split("=")[1])
    
    print("=== 超級大滿貫II 自动打牌 v1.0 ===")
    print(f"最大动作数: {max_actions}")
    print()
    
    # 初始化模块
    inp = InputAdapter()
    scr = ScreenReader()
    det = StateDetector()
    strat = MahjongStrategy()
    exe = ActionExecutor(inp, scr, det)
    rec = RecoveryManager(max_retries=3, fail_threshold=5)
    ctl = GameController(inp, scr, det, strat, exe, rec)
    
    # Phase 1: 确保进入游戏
    print("--- 阶段1: 进入游戏 ---")
    if not ctl.ensure_coins_and_start():
        print("无法进入游戏，停止")
        ctl.save_history(os.path.expanduser("~/workspace/sdmg2-test/logs/auto-play.json"))
        return 1
    
    # Phase 2: 对局循环（牌面识别未实现，需人工介入点）
    print("--- 阶段2: 对局 ---")
    print("注意：自动牌面识别未实现。对局中的打牌决策需人工提供牌面。")
    print("当前实现：状态检测 + 输入执行框架已就绪。")
    
    # 检查当前状态
    img, msg = scr.capture()
    if img:
        state, conf, _ = det.detect(img)
        print(f"当前状态: {state} (conf={conf:.2f})")
        if state == "GAMEPLAY":
            print("检测到对局状态。")
            print("要全自动打牌，需实现 mahjong_vision.py 的牌面识别。")
            print("或手动提供牌面列表，调用 strategy.choose_discard()。")
    
    ctl.save_history(os.path.expanduser("~/workspace/sdmg2-test/logs/auto-play.json"))
    print()
    print("=== 完成（框架验证） ===")
    print("日志: ~/workspace/sdmg2-test/logs/auto-play.json")
    return 0

if __name__ == "__main__":
    sys.exit(main())
