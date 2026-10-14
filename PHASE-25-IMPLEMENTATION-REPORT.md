# 阶段二十五实施报告

**日期**：2026-10-14

## 创建文件

### 程序

- records/__init__.py
- records/schema.py（SQLite 建表）
- records/ledger.py（流水+核对）
- records/pnl.py（统计）
- records/behavior.py（行为模型）
- records/simulator.py（模拟器占位）
- records/tests/test_records.py

### 文档（8 份）

1. GAME-RECORDING-SCHEMA.md
2. CREDIT-LEDGER-AND-PNL.md
3. HUMAN-BEHAVIOR-MODEL.md
4. DOUBLE-UP-DATA-MODEL.md
5. GRAND-SLAM-DATA-MODEL.md
6. SIMULATION-ENGINE-DESIGN.md
7. MODEL-EVALUATION-PLAN.md
8. 本报告

## 测试

**命令**：`python3 records/tests/test_records.py`  
**结果**：4/4 通过（合成数据，明确标记）

## 验收

- [x] 可记录完整事件序列（schema 就绪）
- [x] 可核对流水（ledger.verify）
- [x] 可计算胜率/盈亏/回撤（pnl.py）
- [x] 三模式分别统计（category 区分）
- [x] 未知不静默（UNKNOWN_RULE）
- [x] 真实/模拟分离（is_simulation 标记）
- [x] 可追溯（game_id, event_id）
- [x] 合成数据明确标记
- [x] 测试 4/4 执行
- [x] PID 36644 未影响

## 未解决

- 真实规则未知（比倍/大满贯全 UNKNOWN）
- 无真实牌局数据
- 模拟器占位（规则未知）

## 下一步最需证据

1. 比倍进入条件与档位含义（画面+规则资料）
2. 大满贯触发条件（画面+规则资料）
3. 下注单位确认（1000 的真实含义）
4. 真实牌局记录（需授权实验）
