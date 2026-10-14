# DIP 与 Start 条件报告

**日期**：2026-10-14  
**源码**：igs017.cpp（MAME master，版本差异待确认）

## DSW2 关键位

```
PORT_DIPNAME( 0x40, 0x40, DEF_STR( Controls ) )  // 操作方式 SW2:7
  0x40 = "Mahjong"（按鍵，麻将按钮矩阵）
  0x00 = "Joystick"（搖桿，摇杆+按钮）
```

## Start 条件

```c
PORT_BIT( 0x01, IP_ACTIVE_LOW, IPT_START1 )
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 開始
```

**含义**：IPT_START1（键盘 "1"）仅在 **Joystick 模式**（DSW2 bit 0x40 = 0）时有效。

在 Mahjong 模式（0x40）时，Start 必须通过麻将按钮矩阵触发，具体按钮未知。

## 实测对应

| NVRAM 状态 | DSW2 0x40 | Start("1") | 结果 |
|------------|-----------|------------|------|
| 空白（默认） | 0x40（Mahjong） | 无效 | 符合源码条件 |
| 用户 NVRAM | 0x00（Joystick） | 有效 | 符合源码条件 |

## 结论

1. **Start = "1" 仅在 Joystick 模式有效**（源码确认）
2. 用户机器使用 Joystick 模式（NVRAM 中 DSW2 0x40=0）
3. 空白 NVRAM 默认 Mahjong 模式，Start 需用矩阵按钮

## 待验证

- MAME 0.285 二进制与 master 源码的版本差异
- Mahjong 模式下 Start 对应的矩阵按钮
- "喜從天降"奖励关与 DSW/NVRAM 的关系

## DIP 设置方法核实（2026-10-14）

**DIP 位置**：DSW2 bit 0x40，SW2:7，操作方式
- 0x40 = Mahjong（默认）
- 0x00 = Joystick

**控制方式**：
1. 存储在 NVRAM 中（非 MAME cfg 文件）
2. 可通过 MAME UI（Tab → Dip Switches）修改
3. 无官方命令行参数可直接设置
4. 修改 NVRAM 二进制字节被用户明确禁止

**NVRAM 覆盖**：
- NVRAM 中的 DIP 设置覆盖源码默认值
- 空白 NVRAM 使用源码默认值（Mahjong）
- 用户 NVRAM 已设置为 Joystick（来源：历史游戏设置）

**限制**：
- 无法在不修改 NVRAM 字节的情况下，可靠地将空白 NVRAM 设置为 Joystick 模式
- MAME UI via xdotool 不可靠（Tab 无反应）
