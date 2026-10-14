# 游戏配置模型设计

**日期**：2026-10-14

## GameConfigurationModel

```python
@dataclass
class Setting:
    setting_id: str
    current_value: Any
    default_value: Any
    evidence: str
    verified: bool
    reversible: bool
```

## GameRuleEvidenceStore

存储：
- 来源文件及哈希
- 源码位置
- 截图
- CREDIT/BET 变化
- 证据等级

## 证据等级

- VERIFIED：实测确认
- SUPPORTED：多源支持
- HYPOTHESIS：推测
- UNKNOWN：未知

## 当前已验证

- 按5=CREDIT+1（VERIFIED）
