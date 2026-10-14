# NVRAM 基线报告

**日期**：2026-10-14

## 文件清单

| 文件 | 大小 | 修改时间 | SHA-256（前16） | 用途 | 状态 |
|------|------|----------|----------------|------|------|
| /home/zhangdawei/.mame/nvram/sdmg2754ca/nvram | 64K | Oct 14 06:12 | ad8f2bf5025b9c9a | 原实例（PID 36644） | 使用中，勿动 |
| /tmp/xvfb-test/nvram/nvram | 64K | Oct 14 10:41 | 未记录 | Xvfb 测试（已废弃） | 可能损坏，已清理 |
| nvram-backup-20261014.tar.gz | - | Oct 14 10:35 | - | 奖励关状态 | 不可靠（从运行中复制） |

## 基线定义

**有效基线**：`/home/zhangdawei/.mame/nvram/sdmg2754ca/nvram`
- 对应 PID 36644（运行 2.5 小时+）
- 游戏状态：ODDS，CREDIT 9（主游戏流程）
- DSW2：Joystick 模式（0x40=0），Start("1") 有效
- **不可复制**（运行中使用），不可修改

**无效基线**：
- 空白 NVRAM：Mahjong 模式，Start("1") 无效
- 奖励关 NVRAM：从运行中复制，可能损坏，已废弃

## 实验原则

1. 不复制运行中的 NVRAM（文件可能不一致）
2. 不修改原实例的 NVRAM
3. 新实验用空白 NVRAM + 手动设置 DIP（通过 MAME UI 或配置）
4. 或：等待原实例自然退出后复制（需用户确认）

## 待验证

- 空白 NVRAM + Joystick DIP 是否能进主游戏（不经过奖励关）
- 奖励关是否是 NVRAM 特定状态触发
