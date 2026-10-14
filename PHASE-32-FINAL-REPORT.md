# 阶段三十二最终报告

**日期**：2026-10-14

## 隔离实例

- 测试 PID：76460, 77029, 75477（已清理）
- 原 PID 36644：✅ 存活，未受影响

## 源码验证

**MAME -listxml 输出**：
```xml
<dipswitch name="Controls" tag="DSW2" mask="64">
    <dipvalue name="Mahjong" value="64" default="yes"/>
    <dipvalue name="Joystick" value="0"/>
</dipswitch>
```

**确认**：
- Controls = DSW2 bit 6 (0x40)
- Mahjong = 0x40（默认）
- Joystick = 0x00
- Bet 仅在 Joystick 模式有效（PORT_CONDITION）

## DIP 发现

| 项目 | 值 | 说明 |
|------|-----|------|
| Credit Limit | 2000 | 积分上限，非比倍上限 |
| Controls | Mahjong | 默认模式 |
| Minimum Bet | 1 | 最小下注 |
| Double Up Jackpot | 500 | 比倍奖励 |

## Q-002 结论

**BLOCKED → ROOT CAUSE FOUND**：
- 不是按键映射错误
- 是 **DIP 模式不匹配**
- Mahjong 模式下 Bet (BUTTON2) 被禁用

## 控制器更新

✅ `learning/controller.py` 已加入 DIP 知识：
- DIP_CONTROLS 字典
- Bet 有效性判断逻辑

## 下一步（自动）

1. 在 Joystick 模式下测试 Bet
2. 或研究 Mahjong 模式的下注按键
3. Q-003：主对局进入

## 安全

- ✅ 所有测试实例已清理
- ✅ 原实例未受影响
- ✅ 配置文件独立
