# 状态分类修订（阶段二十六）

**日期**：2026-10-14

## 问题

阶段二十五测试中，检测器将「四暗刻」胡牌展示误判为主对局。

**原因**：底部有牌区，触发了 MAIN_GAME 启发式规则。

## 修订

### 新增状态

| 状态 | 说明 |
|------|------|
| WINNING_HAND_DISPLAY | 胡牌展示（如四暗刻） |
| MAIN_GAME_CANDIDATE | 候选（非已验证） |
| DEMO_OR_ATTRACT | 演示画面 |

### 关键区分

**MAIN_GAME_CANDIDATE ≠ MAIN_GAME**

- 候选：有牌区特征，但未验证可操作
- 已验证：需额外证据（当前无）

### 分类逻辑

1. 底部浅色 >0.15 → 有牌
2. 有牌 → MAIN_GAME_CANDIDATE（非 WINNING_HAND_DISPLAY，因文本特征不可靠）
3. 无牌 → UNKNOWN_STATE

**保守原则**：宁可返回候选，不误判为可操作。

## 测试

- 四暗刻 → MAIN_GAME_CANDIDATE（分类）
- 门禁拦截 → 不可操作 ✅
