# Bet 键位源码审计

**日期**：2026-10-14  
**驱动**：igs017.cpp (sdmg2)  
**MAME**：0.285

## 输入定义

**位置**：igs017.cpp:3858
```c
PORT_BIT( 0x40, IP_ACTIVE_LOW, IPT_BUTTON2 )
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 押注
```

## 字段说明

| 项目 | 值 |
|------|-----|
| 输入项名称 | IPT_BUTTON2 |
| 中文标注 | 押注 (Bet) |
| 输入类型 | 按钮 (Button 2) |
| 端口位 | 0x40 |
| 条件 | DSW2 & 0x40 == 0x00 (Joystick 模式) |
| 源文件 | src/mame/igs/igs017.cpp |
| 行号 | 3858 |

## 键盘默认映射

**源码中未定义**。

驱动源码仅声明逻辑输入类型（IPT_BUTTON2），不指定键盘映射。
键盘映射由 MAME 核心的默认输入配置决定，不在驱动源码中。

**结论**：无法从驱动源码直接确认 Bet 对应的键盘按键。

## 相关输入

| 输入 | 标注 | 条件 |
|------|------|------|
| IPT_START1 | 開始 | Joystick 模式 |
| IPT_BUTTON1 | 摸捨 (Discard) | Joystick 模式 |
| IPT_BUTTON2 | 押注 (Bet) | Joystick 模式 |

## 证据等级

- **源码确认**：IPT_BUTTON2 = 押注，仅 Joystick 模式有效
- **未知**：键盘默认映射（需查 MAME 核心或实际测试）
