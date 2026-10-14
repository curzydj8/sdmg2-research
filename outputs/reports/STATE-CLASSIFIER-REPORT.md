# 状态分类器报告

**日期**：2026-10-14

## 支持状态

| 状态 | 检测方法 | 测试结果 |
|------|----------|----------|
| MAIN_GAME | 底部浅色像素比例 >15% | ✅ 在 bet002-poll3.png 上通过 |
| TITLE | - | ❌ 返回 UNKNOWN（未实现） |
| ODDS | - | ❌ 返回 UNKNOWN（未实现） |
| REWARD | - | ❌ 返回 UNKNOWN（未实现） |
| UNKNOWN | 默认 | ✅ |

## 测试集

- bet002-poll3.png → MAIN_GAME (0.7) ✅
- demoA-t0.png (标题) → UNKNOWN ❌
- bet002-reliable-result.png (ODDS) → UNKNOWN ❌
- demoA-t10.png (奖励关) → UNKNOWN ❌

## 限制

当前仅实现 MAIN_GAME 检测。TITLE/ODDS/REWARD 需要：
- 特定文字识别（"ODDS", "喜從天降"）
- 或特定布局特征

**覆盖范围**：1/5 状态。
