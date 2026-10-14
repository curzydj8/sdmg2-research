# 阶段二十八基线审计

**日期**：2026-10-14

## 项目文件

- Markdown 报告：114 份
- Python 模块：25 个（vision 9, autonomous 10, records 6）
- 测试：autonomous 7/7, records 4/4

## 关键证据

### 阶段二十七（上分验证）

- 测试 PID：73591（已清理）
- 原 PID 36644：未受影响 ✅
- 按 "5" → CREDIT 0→1
- 状态：演示 → ODDS
- **单位**：每次 1 CREDIT（非 1000）

### 阶段二十六（状态分类）

- 门禁 5/5 通过
- MAIN_GAME_CANDIDATE ≠ 可操作

### 输入映射（已知）

| 输入 | 源码 | 含义 |
|------|------|------|
| IPT_BUTTON2 | igs017.cpp:3858 | 押注（Bet） |
| IPT_START1 | 驱动 | 開始 |
| IPT_BUTTON1 | 驱动 | 摸捨 |

**未知**：键盘默认映射（源码未定义）

## 当前实例

- PID 36644：运行中，未触碰
- 无其他测试实例运行

## 数据目录

- /tmp/xvfb-test/round1/（已用）
- /tmp/xvfb-test/topup/（已用）
