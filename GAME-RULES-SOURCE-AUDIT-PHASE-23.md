# 规则来源审计（阶段二十三）

**日期**：2026-10-14

## MAME 驱动源码

**文件**：src/mame/igs/igs017.cpp (mame0285)

**实际存在**：
- ROM 区域声明（sprites, tilemaps, maincpu, oki）
- 输入端口定义（IPT_BUTTON2=Bet 等）
- DIP 开关定义
- 游戏元数据（1997, IGS, V754C）

**不存在**：
- ❌ 麻将规则
- ❌ 胡牌算法
- ❌ 牌型定义
- ❌ 计分规则

**驱动注释**：仅硬件相关，无规则。

## 现有报告

| 报告 | 规则证据 |
|------|----------|
| ROM-DATA-FEASIBILITY-REPORT.md | 无规则 |
| MAHJONG-RULES-EVIDENCE.md | 明确未知 |
| GAME-DATA-SOURCE-DECISION.md | 无规则 |
| MAHJONG-RULE-ENGINE-REPORT.md | 通用规则，非游戏规则 |

## 截图证据

| 截图 | 可见信息 | 规则推断 |
|------|----------|----------|
| bet002-poll3.png | 14 张牌 | 手牌数（非规则） |
| e2e-post-5s.png | 喜從天降，CREDIT 0 | 奖励关存在（规则未知） |
| bet002-reliable-result.png | ODDS 表，CREDIT 1 | 赔率表存在（规则未知） |

**限制**：不能从单张截图推断完整规则。

## 结论

**直接证据**：零条游戏专属规则  
**源码证据**：驱动无规则信息  
**合理推断**：无（不得推断）  
**未知**：全部规则
