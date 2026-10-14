# 视觉样本管理工具

**日期**：2026-10-14

## 工具

`tools/dataset_audit.py`

**用法**：
```bash
python3 tools/dataset_audit.py --index GAME-STATE-CLASSIFIER-DATASET-INDEX.json
```

**功能**：
- 验证文件存在
- 验证 SHA-256
- 验证标签在允许列表
- 验证图片可读取
- 输出审计报告

**允许标签**：MAIN_GAME, REWARD, ODDS, TITLE, UNKNOWN_STATE

## 测试结果

```
样本总数: 4
✅ MAIN_GAME: screenshots/bet002-poll3.png (1003x752)
✅ REWARD: screenshots/e2e-post-5s.png (1003x752)
✅ ODDS: screenshots/bet002-reliable-result.png (1003x752)
✅ TITLE: screenshots/demoA-t0.png (1003x752)
```

**结论**：4/4 有效，无重复，无派生裁切。
