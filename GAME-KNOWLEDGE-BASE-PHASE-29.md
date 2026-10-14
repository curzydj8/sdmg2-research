# 游戏知识库（阶段二十九）

**日期**：2026-10-14

## 基本信息

| 项目 | 值 | 来源 | 可信度 |
|------|-----|------|--------|
| 完整名称 | 超級大滿貫II / Chaoji Da Manguan II | MAME ROM 名 | VERIFIED |
| ROM 短名 | sdmg2754ca | MAME | VERIFIED |
| 版本 | V754C, set 1 | MAME | VERIFIED |
| 开发商 | I.G.S CO., LTD. | 标题画面 | VERIFIED |
| 年份 | 1997 | 标题画面 | VERIFIED |
| 驱动 | igs017.cpp | MAME 源码 | VERIFIED |
| 类型 | 麻将赌博机 | 画面观察 | SUPPORTED |

## 网络检索结果

**检索词**：
- 超级大满贯II 街机 麻将 操作 按键
- Super Grand Slam II IGS arcade mahjong MAME
- 超級大滿貫II IGS 1997 玩法

**结果**：未找到该游戏的专门攻略、说明书或操作资料。

**结论**：这是小众街机游戏，公开资料稀缺。

## MAME 驱动信息

**输入端口**（igs017.cpp:3858）：
- IPT_BUTTON2 = 押注（Bet），仅 DSW2 Joystick 模式
- IPT_START1 = 開始
- IPT_BUTTON1 = 摸捨（Discard）

**硬件**：
- CPU: Motorola MC68000 11 MHz
- Sound: OKI MSM6295
- Video: 512×240, 60Hz

## 直接观察证据

| 画面 | 特征 | 状态 |
|------|------|------|
| 标题 | 超級大滿貫II + 佛像 | TITLE |
| 演示 | 喜從天降奖励循环 | DEMO_OR_ATTRACT |
| ODDS | 赔率表，CREDIT/BET 显示 | ODDS |
| 胡牌展示 | 四暗刻 + 牌 | WINNING_HAND_DISPLAY |

## 实测规则

- 按 "5" → CREDIT +1（VERIFIED）
- 上分后 → ODDS 状态（VERIFIED）
