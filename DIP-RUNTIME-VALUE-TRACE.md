# DIP 运行时值追踪

**日期**：2026-10-14

## 源码路径

**定义**（mame0285/src/mame/igs/igs017.cpp:3823）：
```c
PORT_DIPNAME( 0x40, 0x40, DEF_STR( Controls ) )  // SW2:7 操作方式
  PORT_DIPSETTING( 0x40, "Mahjong" )  // 默认
  PORT_DIPSETTING( 0x00, DEF_STR( Joystick ) )
```

**使用**（sdmg2 INPUT_PORTS）：
```c
PORT_BIT( 0x01, IP_ACTIVE_LOW, IPT_START1 )
  PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)  // 開始
```

## 值流转路径（理论）

1. **驱动声明默认值**：0x40（Mahjong）
   - 来源：PORT_DIPNAME 第二个参数
   - 证据：源码确认

2. **MAME 配置文件**：/home/zhangdawei/.mame/cfg/sdmg2754ca.cfg
   - 内容：20 行，仅 mixer/video，无 DIP 设置
   - 证据：实测文件内容
   - 结论：使用默认值

3. **运行时值**：应为 0x40（Mahjong）
   - 推理：cfg 无覆盖 → 用默认
   - 证据：间接（cfg 内容）

4. **实际行为**：Start("1") 有效
   - 实测：用户 NVRAM 下按 "1" 有反应
   - 矛盾：按源码，Mahjong 模式下 Start 应无效

## 差异分析

**源码默认值**：Mahjong (0x40) → Start 无效  
**实际行为**：Start 有效 → 应为 Joystick (0x00)  
**差异**：无法解释

**可能原因**（未证实）：
1. cfg 文件非实际使用文件（但命令行无 -cfg_directory）
2. MAME 有其他 DIP 存储位置（未找到）
3. 游戏 NVRAM 覆盖 DIP（源码无证据）
4. 对 PORT_CONDITION 理解有误（需验证）

## 证据等级

- **源码确认**：DIP 定义、默认值、Start 条件
- **运行时实测**：cfg 内容、Start 有效性
- **合理推断**：应为 Mahjong 模式（基于 cfg）
- **仍未知**：实际 DSW2 值、差异原因

## 需进一步确认

1. MAME 运行时实际 DSW2 值（需调试接口）
2. 是否有其他 cfg 文件被加载
3. PORT_CONDITION 的精确语义
