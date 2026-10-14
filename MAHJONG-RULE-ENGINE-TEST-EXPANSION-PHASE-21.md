# 规则引擎测试扩展（阶段二十一）

**日期**：2026-10-14

## 新增测试（7 个）

| 测试 | 内容 | 结果 |
|------|------|------|
| test_invalid_tile_code | 非法牌值 | ✅ |
| test_hand_too_long | 超 14 张 | ✅ |
| test_winning_with_sequences | 顺子胡牌 | ✅ |
| test_not_winning_incomplete | 13 张非胡 | ✅ |
| test_ting_multiple_waits | 听牌 | ✅ |
| test_discard_no_duplicates | 出牌去重 | ✅ |
| test_input_not_mutated | 输入不修改 | ✅ |

## 总测试数

- 基础：4
- 规则：4
- 扩展：7
- **总计：15/15 通过**

## 覆盖

✅ 非法输入  
✅ 边界条件  
✅ 胡牌正例/反例  
✅ 听牌  
✅ 输入不变性

## 未覆盖

- 七对、国士等特殊牌型
- 副露
- 多规则切换
