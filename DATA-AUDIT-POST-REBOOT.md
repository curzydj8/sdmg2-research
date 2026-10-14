# 数据审计报告（重启后）

**日期**：2026-10-14 21:00 CST
**事件**：用户于 20:28 重启 Ubuntu，/tmp 被清空

## 已确认保存的数据

| 数据 | 位置 | 状态 |
|------|------|------|
| 学习模块 | ~/workspace/sdmg2-test/learning/ | ✅ 完整 |
| 检查点 | learning/checkpoints.json | ✅ 完整 |
| 监督器 | supervisor.py | ✅ 运行中 |
| 148 份文档 | ~/workspace/sdmg2-test/*.md | ✅ 完整 |
| 关键截图 | ~/workspace/sdmg2-test/screenshots/ (114 个) | ✅ 含 auto-last、resume 系列 |
| 审计报告 | DATA-AUDIT-24H-REPORT.md 等 | ✅ 完整 |

## 已丢失的数据

| 数据 | 原因 |
|------|------|
| /tmp/xvfb-test/auto/screenshots/ 92 张截图 | 重启清空 /tmp，仅 1 张新实例截图残留 |
| auto_play.py 运行日志 | /tmp 日志丢失（本就为空） |
| MAME 实例内存状态 | 进程终止，不可恢复 |

## 无法恢复 vs 可恢复

- ❌ **原牌局**：MAME 无存档机制，内存状态随进程终止丢失，不可恢复
- ❌ **PID 36644**：用户重启已终止，不存在了
- ✅ **学习进度**：检查点、规则库、任务列表完整，可恢复
- ✅ **当前实例**：PID 20096，新隔离实例运行中，已过信息屏

## 结论

牌局进度不可恢复（游戏设计如此），但全部学习成果完整保留。新实例已启动，24h 监督器运行中。
