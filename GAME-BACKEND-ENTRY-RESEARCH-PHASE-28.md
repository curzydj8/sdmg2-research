# 游戏后台入口研究

**日期**：2026-10-14

## MAME 设置

### 输入映射

**驱动源码**（igs017.cpp:3858）：
```c
PORT_BIT(0x40, IP_ACTIVE_LOW, IPT_BUTTON2)
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 押注
```

**已知**：
- Bet = IPT_BUTTON2（逻辑类型）
- 仅 DSW2 & 0x40 == 0x00 时有效（Joystick 模式）

**未知**：
- 键盘默认映射（源码未定义）
- 运行时实际绑定

### DIP Switch

- DSW2 存在（条件引用）
- 具体选项：UNKNOWN（需查驱动）

## 游戏内部设置

| 入口 | 状态 |
|------|------|
| Service Mode | UNKNOWN |
| Test Mode | UNKNOWN |
| 设置菜单 | UNKNOWN |

**结论**：无可靠证据确认游戏内部设置入口。

## MAME 菜单 vs 游戏菜单

- MAME Tab 菜单：模拟器配置（输入映射等）
- 游戏服务菜单：街机主板功能
- **二者不同**，不得混淆

## 限制

- 无驱动源码访问（远程无源码）
- 不得修改 ROM/NVRAM 寻找设置
