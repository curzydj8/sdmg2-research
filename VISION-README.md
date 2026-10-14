# 超级大满贯Ⅱ视觉识别系统

## 结构

```
vision/           # 识别模块
datasets/         # 数据集
outputs/          # 输出（json/overlays/reports）
tests/            # 单元测试
tools/            # 工具脚本
```

## 使用

```bash
# 单张处理
python3 -m vision.pipeline --input screenshots/example.png --output outputs

# 输出：
# - outputs/json/<name>-result.json
# - 状态分类、牌区检测、单牌定位
```

## 模块

- `capture_loader.py`: 截图加载
- `state_classifier.py`: 状态分类（仅 MAIN_GAME 可用）
- `hand_region.py`: 牌区定位（相对坐标）
- `tile_detector.py`: 单牌分割（等宽 14 份）
- `tile_classifier.py`: 牌面识别（占位，未实现）
- `consistency_check.py`: 一致性验证

## 限制

- 状态分类：仅 MAIN_GAME 可靠
- 牌面识别：未实现（返回 UNKNOWN_TILE）
- 需人工标注建立模板库
