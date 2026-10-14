# 自主游戏学习架构

**日期**：2026-10-14  
**版本**：0.1.0

## 模块

| 模块 | 文件 | 职责 |
|------|------|------|
| ObservationEngine | autonomous/observation.py | 读取截图，识别状态，输出 GameObservation |
| GameStateMachine | autonomous/state_machine.py | 12 候选状态，证据追踪 |
| RuleHypothesisEngine | autonomous/hypothesis.py | 5 级证据，E 级不允许决策 |
| ActionPlanner | autonomous/planner.py | 只规划，不执行 |
| OutcomeVerifier | autonomous/verifier.py | 对比前后，区分因果 |
| ExperienceMemory | autonomous/memory.py | 结构化记录，保留矛盾 |

## 学习闭环

```
观察 → 识别状态 → 提出假设 → 预测 → 检查证据 → 生成计划 → 授权检查 → [执行禁用] → 验证 → 更新经验
```

## 模式

| 模式 | 允许 |
|------|------|
| OBSERVE_ONLY | ✅ |
| ANALYZE | ✅ |
| SIMULATE | ✅ |
| PLAN_ONLY | ✅ |
| CONTROLLED_TEST | ❌（需单独授权） |
| AUTONOMOUS_PLAY | ❌（未来目标） |

## 测试

`python3 autonomous/tests/test_autonomous.py` → 7/7 通过
