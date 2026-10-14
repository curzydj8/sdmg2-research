# 视觉识别阶段七最终报告

**日期**：2026-10-14

## 项目结构

**修改前**：无 vision/ 目录，有 modules/mahjong_vision.py（旧代码）
**修改后**：
```
vision/           # 新建，9 个模块
datasets/         # 新建，4 个子目录
outputs/          # 新建，json/overlays/reports
tests/            # 新建（空）
tools/            # 新建（空）
```

**新建文件**：
- vision/__init__.py, capture_loader.py, state_classifier.py
- vision/hand_region.py, tile_detector.py, tile_classifier.py
- vision/confidence.py, consistency_check.py, pipeline.py
- VISION-README.md

**复用**：参考了 modules/mahjong_vision.py 的牌区相对坐标方法

## 执行命令

```bash
mkdir -p vision datasets/{raw,labeled,tile_templates,manifests} ...
python3 -m vision.pipeline --input screenshots/bet002-poll3.png --output outputs
```

## 测试结果

**状态分类**：
- MAIN_GAME: ✅ (bet002-poll3.png, conf 0.7)
- TITLE/ODDS/REWARD: ❌ (返回 UNKNOWN，未实现)

**手牌检测**：
- 输入：1003x752 截图
- 输出：14 张牌，每张 67x120，bbox 为全图坐标
- 一致性：通过

**牌面识别**：
- 状态：未实现（占位）
- 输出：全部 UNKNOWN_TILE，需人工复核

## 已知问题

1. 状态分类器仅支持 MAIN_GAME
2. 牌面分类器未实现
3. 无标注模板库
4. 未处理非 14 张的异常情况

## 准确率

**无法测量**。无人工标注真值，只能报告：
- 检测率：14/14（100%，单样本）
- 待复核比例：100%（牌面未识别）

## 未解决

- TITLE/ODDS/REWARD 分类
- 牌面模板匹配
- 牌数异常处理

## 下一步

1. 人工标注现有截图的牌面
2. 建立 tile_templates/
3. 实现 OpenCV 模板匹配
4. 扩展状态分类器
