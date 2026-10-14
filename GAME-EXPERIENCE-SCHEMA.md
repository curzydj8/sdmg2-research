# 经验记录模式

**日期**：2026-10-14

## ExperienceRecord 字段

| 字段 | 说明 |
|------|------|
| session_id | 会话 ID |
| env_id | 测试环境标识 |
| game_state | 游戏状态 |
| screenshot_sha_before | 输入前截图哈希 |
| screenshot_sha_after | 输入后截图哈希 |
| known_vars | 已知变量（CREDIT 等） |
| action | 动作及授权依据 |
| expected | 预期结果 |
| actual | 实际结果 |
| failure_reason | 失败原因 |
| repeatable | 是否可重复 |
| next_suggestion | 下一步建议 |

## 存储

`autonomous/experience.jsonl`（JSON Lines）

## 原则

- 成功和失败都保留
- 矛盾结果不覆盖
- 可追溯到原始截图
