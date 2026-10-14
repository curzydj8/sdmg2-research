# 按键映射参考（阶段二十九）

**日期**：2026-10-14

## 用户提供的线索（待验证）

| 按键 | 网络资料作用 | MAME 映射 | 实测 | 证据等级 |
|------|--------------|-----------|------|----------|
| 5 | 上分 | Coin | CREDIT+1 ✅ | VERIFIED |
| 1 | 开始 | UNKNOWN | 未测试 | HYPOTHESIS |
| 2 | 押分 | UNKNOWN | 未测试 | HYPOTHESIS |
| 6 | 下分 | UNKNOWN | 未测试 | HYPOTHESIS |
| TAB | 设置/菜单 | MAME 菜单 | 未测试 | HYPOTHESIS |
| A-N | 牌操作 | UNKNOWN | 未测试 | HYPOTHESIS |
| Left Ctrl | 杠 | UNKNOWN | 未测试 | HYPOTHESIS |
| Left Alt | 碰 | UNKNOWN | 未测试 | HYPOTHESIS |
| Space | 吃 | UNKNOWN | 未测试 | HYPOTHESIS |
| Left Shift | 听牌 | UNKNOWN | 未测试 | HYPOTHESIS |
| Z | 胡牌 | UNKNOWN | 未测试 | HYPOTHESIS |
| Esc | 退出 | UNKNOWN | 未测试 | HYPOTHESIS |

## 已确认

- **"5"**：上分，CREDIT+1（阶段二十七实测）

## TAB 特别说明

TAB 可能打开 MAME 模拟器菜单，而非游戏设置。
**必须区分**：
- MAME 菜单：模拟器配置
- 游戏服务菜单：街机主板功能
- 游戏设置：游戏程序配置

## 驱动确认的输入

| 输入 | 含义 | 条件 |
|------|------|------|
| IPT_BUTTON2 | 押注 | DSW2 Joystick 模式 |
| IPT_START1 | 開始 | DSW2 Joystick 模式 |
| IPT_BUTTON1 | 摸捨 | DSW2 Joystick 模式 |

**键盘映射**：源码未定义，UNKNOWN。
