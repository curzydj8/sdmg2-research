# Bet 映射机制追踪

**日期**：2026-10-14

## 调用链（已确认部分）

```
驱动定义 (igs017.cpp:3858)
  ↓ PORT_BIT(0x40, IP_ACTIVE_LOW, IPT_BUTTON2) // 押注
  ↓
输入端口初始化 (ioport.cpp)
  ↓ ioport_manager::initialize()
  ↓ init_port_types()
  ↓ emplace_core_types(m_typelist)  ← 关键函数
  ↓
??? (未找到定义)
```

## 已检查位置

| 文件 | 内容 | 结果 |
|------|------|------|
| src/emu/ioport.h | ioport_type 定义 | 无映射表 |
| src/emu/ioport.cpp | init_port_types(), emplace_core_types() 调用 | 调用存在，定义未找到 |
| src/emu/input.cpp | input_type_entry | 仅 joystick ID |
| src/emu/inptport.cpp | - | 无相关 |

## 卡住环节

**`emplace_core_types` 定义未找到**。

该函数负责填充默认输入类型列表（含键盘映射），但：
- 不在 ioport.cpp 中定义
- 不在 ioport.h 中声明（grep 无结果）
- 可能在其他文件或为模板函数

## 工作量评估

**若继续追踪**：
- 需下载完整 MAME 0.285 源码树（~2GB）
- 需在本地搜索所有文件
- 预计：2-4 小时

**风险**：低（只读搜索）

## 替代方案

**MAME UI 查看**（未尝试）：
- Tab → Input Settings 可显示绑定
- 但 Tab 在 Xvfb 下无反应
- 需解决 UI 访问问题

## 结论

映射机制链条**部分中断**，无法通过现有单文件 curl 方法完成追踪。
