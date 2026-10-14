# 阶段二十六测试报告

**日期**：2026-10-14

## 测试执行

**命令**：
```bash
python3 -c "from vision.state_classifier import classify_state, is_actionable_state; ..."
```

## 结果

| 测试 | 结果 |
|------|------|
| 四暗刻门禁拦截 | ✅ |
| CREDIT=0 拦截 | ✅ |
| 候选状态拦截 | ✅ |
| UNKNOWN 拦截 | ✅ |
| 缺失文件 | ✅ |

**通过**：5/5

## 样本

- 真实：screenshots/round1-pre-coin.png（四暗刻）
- 真实：screenshots/bet002-poll3.png（主对局候选）

## 遗留问题

1. WINNING_HAND_DISPLAY 文本特征不可靠（方差区分度不足）
2. 当前用 MAIN_GAME_CANDIDATE + 门禁拦截作为保守方案
3. 需更多样本或 OCR 才能精确区分

## 结论

**能否可靠区分**：
- 演示 vs 胡牌展示 vs 可玩：⚠️ 部分（靠门禁兜底）
- 精确分类：❌ 需更多工作

**下一轮需要**：
1. 上分流程授权（验证 CREDIT_ENTRY）
2. 更多状态样本
3. OCR 或模板匹配
