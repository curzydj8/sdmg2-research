# DIP 存储与控制报告

**日期**：2026-10-14  
**MAME 版本**：0.285（运行中），源码核对：mame0285 标签

## 源码证据（mame0285/src/mame/igs/igs017.cpp）

**DIP 定义**：
```c
PORT_DIPNAME( 0x40, 0x40, DEF_STR( Controls ) )  // SW2:7 操作方式
  PORT_DIPSETTING( 0x40, "Mahjong" )  // 按鍵（默认）
  PORT_DIPSETTING( 0x00, DEF_STR( Joystick ) )  // 搖桿
```

**Start 条件**：
```c
PORT_BIT( 0x01, IP_ACTIVE_LOW, IPT_START1 )
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 開始
```
含义：仅当 (DSW2 & 0x40) == 0x00（Joystick 模式）时，键盘 "1" 有效。

## 实测事实

| 条件 | NVRAM | Start("1") | 推断模式 |
|------|-------|------------|----------|
| 空白 NVRAM | 无 | 无效 | Mahjong（默认） |
| 用户 NVRAM | ad8f2bf5... | 有效 | Joystick |

## 存储位置：尚未确认

**已排除**：
- ❌ MAME .cfg 文件（/home/zhangdawei/.mame/cfg/sdmg2754ca.cfg 无 DIP 设置）
- ❌ 命令行参数（启动命令无 DIP 相关选项）

**未确认**：
- ❓ 游戏 NVRAM 是否存储 DIP 覆盖值
- ❓ MAME 是否有其他 DIP 存储位置
- ❓ 用户是否曾通过 UI 修改 DIP（无记录）

**矛盾**：
- 源码默认 Mahjong 模式，Start 应无效
- 但用户 NVRAM 下 Start 有效
- cfg 文件无 DIP 设置
- **无法解释差异，存储位置尚未确认**

## 版本一致性

- 运行版本：0.285
- 源码版本：mame0285 标签
- DIP 定义一致，无版本差异

## 结论

DIP 的真实存储位置**尚未确认**。不能断定其在 NVRAM 中，也不能排除其他机制。
需要进一步证据（如：MAME 运行时 DIP 查询、UI 交互记录）。
