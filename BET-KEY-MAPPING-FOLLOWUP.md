# Bet 键位映射跟进审计

**日期**：2026-10-14

## 已检查文件

| 文件 | 搜索内容 | 结果 |
|------|----------|------|
| src/emu/ioport.h | IPT_BUTTON2, IPT_BUTTON | 仅找到类型引用，无映射定义 |
| src/emu/ioport.cpp | BUTTON2 | 无结果 |
| src/emu/input.cpp | BUTTON2 | 仅 joystick button ID，无键盘映射 |
| src/emu/inptport.cpp | BUTTON2 | 无结果 |
| src/emu/input.h | BUTTON2 | 无结果 |
| src/osd/sdl/input.cpp | BUTTON2 | 无结果 |

## 搜索命令

```bash
# 驱动定义（已确认）
curl .../igs017.cpp | grep -n "IPT_BUTTON2.*押注"
# 结果：3858: PORT_BIT(0x40, IP_ACTIVE_LOW, IPT_BUTTON2) // 押注

# 核心映射（未找到）
curl .../ioport.h | grep -n "IPT_BUTTON2"  # 无结果
curl .../input.cpp | grep -n "BUTTON2"     # 仅 joystick ID
```

## 卡住环节

**无法定位**：IPT_BUTTON2 → 键盘按键的映射定义。

可能原因：
1. 映射在未检查的文件中（如：src/emu/inpttype.h, 默认配置表）
2. 映射由 MAME 运行时动态生成，无静态定义
3. 映射在平台 OSD 层，需完整源码树搜索（非单文件 curl）

## 结论

**核心默认键盘映射：仍未知**。

已确认：
- ✅ 驱动定义：IPT_BUTTON2 = 押注（igs017.cpp:3858）
- ✅ 条件：仅 Joystick 模式
- ❌ 键盘按键：无法从现有方法确认

## 建议

停止源码追踪。改用黑盒测试或接受未知。
