# 上分测试日志（阶段二十七）

**日期**：2026-10-14  
**测试实例 PID**：73591（已清理）  
**原实例 PID 36644**：✅ 未受影响

## 测试步骤

### 1. 启动观察

- **画面**：MAME 信息屏 → 标题 → 喜從天降演示循环
- **初始 CREDIT**：0
- **初始 BET**：0
- **状态**：DEMO_OR_ATTRACT（演示模式）

### 2. 上分操作

- **动作**：按 "5"（投币键）
- **依据**：MAME 标准投币键，阶段四历史成功
- **前截图**：screenshots/topup/screenshots/pre-5.png
- **后截图**：screenshots/topup-post-5.png

### 3. 结果验证

| 项目 | 前 | 后 | 变化 |
|------|----|----|------|
| CREDIT | 0 | 1 | +1 ✅ |
| 状态 | 演示 | ODDS | ✅ |
| BET | 0 | 0 | 无 |

**结论**：上分成功，每次按 "5" 增加 1 CREDIT。

## 重要发现

**用户假设修正**：
- 假设：每次上分 1000
- 实际：每次按 "5" = 1 CREDIT
- **"top_up_amount = 1000" 参数不适用于本游戏**

## 门禁判定

- 分类器：UNKNOWN_STATE（ODDS 模板未实现）
- 门禁：❌ 禁止操作（状态未知）
- **正确**：本阶段仅授权上分，不授权下注

## 截图

- topup-startup.png：信息屏
- topup-after-click.png：标题
- topup-t15s.png：喜從天降演示
- topup-t35s.png：演示继续
- topup-post-5.png：ODDS，CREDIT=1
