# 可玩状态门禁设计

**日期**：2026-10-14

## 函数

`is_actionable_state(classification, credit, bet) -> (bool, reason)`

## 门禁条件（全部满足才允许）

1. 状态已确认（非 UNKNOWN、非候选、非演示/展示/奖励/暂停）
2. CREDIT 已读取且 >0
3. 有明确可操作证据
4. 当前：无已验证的可操作状态 → 全部拒绝

## 禁止列表

- UNKNOWN_STATE
- MAIN_GAME_CANDIDATE（候选≠可操作）
- DEMO_OR_ATTRACT
- WINNING_HAND_DISPLAY
- REWARD, ODDS, PAUSED

## 测试

✅ 四暗刻被拦截  
✅ CREDIT=0 被拦截  
✅ 候选状态被拦截  
✅ UNKNOWN 被拦截
