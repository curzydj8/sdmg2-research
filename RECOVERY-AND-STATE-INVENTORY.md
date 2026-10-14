# 恢复与状态库存

**日期**：2026-10-14 11:00 CST

## 运行实例

| PID | 命令 | 运行时间 | DISPLAY | 状态 |
|-----|------|----------|---------|------|
| 36644 | mame sdmg2754ca -rompath /home/zhangdawei/roms -window | 2h30m | :0 (Wayland/XWayland) | 运行中，ODDS 画面，CREDIT 9 |
| 57319 | Xvfb :99 -screen 0 1280x800x24 | - | :99 | 运行中，无 MAME |

**注意**：Xvfb 中的 MAME 已全部清理，无残留。

## NVRAM 文件

| 路径 | 大小 | 修改时间 | SHA-256（前16） | 状态 |
|------|------|----------|----------------|------|
| /home/zhangdawei/.mame/nvram/sdmg2754ca/nvram | 64K | Oct 14 06:12 | ad8f2bf5025b9c9a | 原实例使用中，勿动 |
| /tmp/xvfb-test/nvram/nvram | 64K | Oct 14 10:41 | （从运行中复制，可能损坏） | 已废弃 |
| ~/workspace/sdmg2-test/nvram-backup-20261014.tar.gz | - | Oct 14 10:35 | - | 奖励关状态备份 |

## 配置

| 路径 | 用途 |
|------|------|
| /home/zhangdawei/.mame/cfg/sdmg2754ca.cfg | 原实例配置（无自定义输入映射） |
| /tmp/xvfb-test/config/ | Xvfb 测试配置（已复制原配置） |

## 关键截图

- screenshots/bonus-current.png：奖励关"喜從天降"（左5-9）
- screenshots/bonus-start.png：奖励关（右1-5，Start 推进后）
- screenshots/xvfb-game4.png：ODDS，CREDIT 1（投币验证）

## 对应关系

- PID 36644 ↔ /home/zhangdawei/.mame/nvram/sdmg2754ca/nvram ↔ 原配置
- Xvfb 测试 ↔ /tmp/xvfb-test/ ↔ 已清理
- 备份 ↔ nvram-backup-20261014.tar.gz ↔ 奖励关状态（已废弃，不可靠）
