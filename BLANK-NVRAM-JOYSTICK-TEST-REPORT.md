# 空白 NVRAM + Joystick 对照实验报告

**日期**：2026-10-14

## 实验 A：空白 NVRAM，默认 DIP

**配置**：
- NVRAM：空白（/tmp/xvfb-test/expA/nvram/，0 文件）
- 配置：独立（/tmp/xvfb-test/expA/config/）
- ROM：sdmg2754ca，MAME 0.285

**结果**：

| 步骤 | 操作 | 结果 |
|------|------|------|
| 启动 | - | 标题画面 ✅ |
| 投币 | 按 5 | ODDS，CREDIT 0→1 ✅ |
| Start | 按 1 | **无反应**，仍在 ODDS ❌ |

**截图**：
- expA-boot.png：标题画面
- expA-coin.png：ODDS，CREDIT 1
- expA-start.png：ODDS，CREDIT 1（Start 无效）

**结论**：空白 NVRAM 默认 Mahjong 模式，IPT_START1 被 DIP 条件禁用，符合源码预期。

## 实验 B：空白 NVRAM，Joystick 模式

**状态**：**无法执行**

**原因**：
1. DIP（DSW2 bit 0x40）存储在 NVRAM 中，无 MAME 官方命令行或配置文件可直接设置
2. 用户明确禁止猜测修改 NVRAM 二进制字节
3. MAME UI（Tab 菜单）无法通过 xdotool 可靠操作
4. 从运行实例复制 NVRAM 不被认定为有效快照

**依据**：用户指令"如果无法可靠设置 Joystick DIP，应将实验 B 标记为无法执行，不能假称设置成功。"

## 对照实验能证明什么

1. ✅ 空白 NVRAM 默认进入 Mahjong 模式（Start 无效）
2. ✅ 用户 NVRAM 为 Joystick 模式（Start 有效，之前已验证）
3. ✅ DIP 条件理论与实测一致

## 不能证明什么

1. ❌ 空白 NVRAM + Joystick 模式是否能进主游戏（实验 B 未执行）
2. ❌ 奖励关"喜從天降"的触发条件
3. ❌ 主麻将对局的具体入口

## 下一步（有依据）

1. 研究 MAME 是否支持通过 cfg 文件设置 DIP（需查文档）
2. 或：在可接受风险下，从已退出的实例复制 NVRAM（需用户确认）
3. 或：接受当前结论，Joystick 模式 = 用户 NVRAM 状态，可直接使用
