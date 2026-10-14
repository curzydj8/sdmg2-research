# 状态分类基线报告（阶段二十一）

**日期**：2026-10-14

## 基线实现

**方法**：无 OCR，仅用已验证视觉特征
- MAIN_GAME：底部浅色比例 >0.15（已验证）
- REWARD/ODDS/TITLE：返回 UNKNOWN（无可靠特征）

## 测试结果

### 正面测试（4 样本）

| 实际 | 预测 | 结果 |
|------|------|------|
| MAIN_GAME | MAIN_GAME | ✅ |
| REWARD | UNKNOWN_STATE | ❌（保守） |
| ODDS | UNKNOWN_STATE | ❌（保守） |
| TITLE | UNKNOWN_STATE | ❌（保守） |

### 负面测试

| 测试 | 结果 |
|------|------|
| 缺失文件 | UNKNOWN_STATE ✅ |
| 空路径 | UNKNOWN_STATE ✅ |

## 限制

- 4 样本同时用于开发，不能视为独立测试集
- 不能证明泛化能力
- REWARD/ODDS/TITLE 需 OCR 或更多特征

## OCR 评估

**未安装**：tesseract/pytesseract 均无  
**不安装**：按约束  
**未来选项**：
- tesseract + chi_sim 语言包（中文）
- 需验证像素字体的识别率
- 需评估置信度阈值
