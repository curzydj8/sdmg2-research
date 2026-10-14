# 视觉识别阶段八最终报告

**日期**：2026-10-14

## 新建/修改文件

**新建**：
- tools/label_tiles.py（标注工具）
- datasets/manifests/tile-labels.jsonl（14 条待标注记录）
- outputs/reports/TILE-LABELING-REPORT.md

**修改**：
- vision/pipeline.py（增加牌面裁切图保存、SHA-256记录）

## 标注样本

- **总数**：14
- **已确认**：0
- **UNKNOWN**：14
- **原因**：裁切图仅 67x120 像素，模糊无法辨认

## 模板库

**未建立**。无可靠标注样本，无法生成模板。

## 识别算法

**未实现**。牌面分类器仍为占位（返回 UNKNOWN_TILE）。

## 测试集

**未划分**。无标注数据，无法评估准确率。

## 运行命令

```bash
python3 -m vision.pipeline --input screenshots/bet002-poll3.png --output outputs
# 输出：14 张牌裁切图，JSON 含 bbox 和 UNKNOWN 标签
```

## 未解决

1. 牌面图像质量不足
2. 无人工标注真值
3. 模板匹配未实现
4. 准确率无法测量

## 下一步

**选项 A**：获取高分辨率截图（需修改 MAME 窗口大小或截图方法）
**选项 B**：接受限制，视觉识别暂停
**选项 C**：使用游戏 ROM 中的牌面图形直接提取模板（需逆向）

**推荐**：选项 B。当前截图质量不足以支持可靠牌面识别。
