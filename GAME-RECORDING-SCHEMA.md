# 牌局记录模式

**日期**：2026-10-14

## 数据模型

| 模型 | 表 | 说明 |
|------|-----|------|
| GameSession | game_sessions | 会话，top_up_amount=1000（用户配置） |
| GameRound | game_rounds | 单局，game_id 唯一 |
| GameEvent | game_events | 事件序列，event_id 唯一 |
| CreditLedger | credit_ledger | 积分流水，不可覆盖 |
| ObservationRecord | （JSONL） | 截图+识别+置信度 |
| RuleEvidence | （JSONL） | 规则假设+证据等级 |
| StrategyDecision | （JSONL） | 候选动作+理由+预测 |
| OutcomeRecord | （JSONL） | 结算+核对 |
| HumanBehaviorProfile | （内存） | 行为统计 |
| SimulationRun | （JSONL） | 模拟批次，标记非真实 |

## 存储

- SQLite：结构化查询（session_id, game_id, 时间）
- JSONL：事件流，便于检查导出

## 实现

- records/schema.py：建表
- records/ledger.py：流水记录与核对
