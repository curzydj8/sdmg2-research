# DIP 开关重大发现

**日期**：2026-10-14  
**实例 PID**：75477

## DIP 设置

| 项目 | 值 |
|------|-----|
| Coinage | 1 Coin/1 Credit |
| Key-In Rate | 10 |
| **Credit Limit** | **2000** |
| Credit Mode | Coin Acceptor |
| Payout Mode | Return Coins |
| Demo Sounds | On |
| Double Up Jackpot | 500 |
| Minimum Bet | 1 |
| Double Up Game | On |
| Double Up Game Name | Continue Play |
| **Controls** | **Mahjong** |
| Number Type | Numbers |

## 关键发现

### 1. Credit Limit = 2000

用户提到的"比倍上限 2000"实际上是 **Credit Limit**（积分上限），不是比倍上限。

### 2. Controls = Mahjong（非 Joystick）

**这是 Bet 失效的原因**！

驱动源码：
```c
PORT_BIT(0x40, IP_ACTIVE_LOW, IPT_BUTTON2)
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 押注
```

Bet 仅在 **Joystick 模式**（DSW2 & 0x40 == 0x00）有效。

当前 DIP 设置为 **Mahjong** 模式，因此 Bet 输入被禁用！

### 3. 在 Mahjong 模式下的输入

需要使用麻将面板按键（A-N 等），而非 Joystick 按钮。

## 结论

Q-002 阻塞原因找到：
- 不是按键映射错误
- 而是 **DIP 模式不匹配**

**解决方案**：
- 将 Controls 改为 Joystick，或
- 使用 Mahjong 模式的对应按键

## 证据等级

- DIP 设置：VERIFIED（截图）
- 模式影响：SOURCE_SUPPORTED（驱动源码）
