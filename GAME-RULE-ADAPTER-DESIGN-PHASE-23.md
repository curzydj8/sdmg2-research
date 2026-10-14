# 规则适配器设计（阶段二十三）

**日期**：2026-10-14  
**状态**：接口设计，未实现游戏专属规则

## 设计原则

1. 通用规则与游戏专属规则分离
2. 未知规则不得静默套用默认值
3. 每条规则可追溯到证据
4. 未确认规则调用返回 UNIMPLEMENTED
5. 视觉分类器不得触发游戏操作

## 接口设计

```python
class RuleAdapter:
    """游戏规则适配器"""
    
    def __init__(self, game_id="sdmg2754ca"):
        self.game_id = game_id
        self._rules = {}  # 规则名 -> (实现, 证据)
    
    def register_rule(self, name, impl, evidence):
        """注册规则实现与证据"""
        self._rules[name] = (impl, evidence)
    
    def is_winning_hand(self, tiles):
        """胡牌判断"""
        if "win" not in self._rules:
            return (None, "UNIMPLEMENTED: win rule not confirmed")
        impl, evidence = self._rules["win"]
        return impl(tiles)
    
    def get_evidence(self, rule_name):
        """获取规则证据"""
        if rule_name not in self._rules:
            return None
        return self._rules[rule_name][1]
```

## 使用示例

```python
# 通用测试规则（当前）
adapter = RuleAdapter()
adapter.register_rule(
    "win",
    generic_win_check,
    evidence="Generic 4m1p, NOT game-specific"
)

# 游戏专属规则（未来，需证据）
# adapter.register_rule(
#     "win",
#     sdmg2_win_check,
#     evidence="Game manual p.XX or verified sample"
# )
```

## 约束

- 不得在未确认时注册游戏规则
- 证据必须为文件路径或可验证来源
- UNIMPLEMENTED 不得被调用方忽略
