# 输入链路诊断（阶段十四）

**日期**：2026-10-14

## 测试环境

- **显示**：Xvfb :99
- **接收器**：xev (Event Tester)
- **输入工具**：xdotool
- **目标**：独立测试窗口（非 MAME）

## 测试结果

### 测试 1：无焦点 + --window 指定

- **发送**：5 次 `xdotool key --window $WID a`
- **接收**：0 个 KeyPress 事件
- **结论**：❌ --window 参数不足以投递事件

### 测试 2：有焦点 (windowactivate)

- **发送**：3 次 `xdotool key a`（焦点已激活）
- **接收**：5 个 KeyPress 事件（synthetic YES）
- **结论**：✅ 焦点激活后事件可投递

## 关键发现

1. **焦点是必需的**：`xdotool windowactivate` 后事件才能到达
2. **--window 不充分**：仅指定窗口 ID 不保证投递
3. **事件为 synthetic**：XTest 生成，非物理键盘（预期内）

## 结果边界

**已验证**：
> "输入工具到独立测试窗口的事件路径已验证（需焦点激活）。"

**不得宣称**：
- ❌ MAME 已收到事件
- ❌ 游戏按键映射已确认
- ❌ 游戏状态已改变
- ❌ 自动打牌可行

## 未解决问题

- MAME 窗口的焦点行为是否与 xev 一致
- XTest 事件是否被 MAME 正确处理（需 MAME 侧验证）
- Wayland vs X11 差异（本测试仅 Xvfb/X11）
