# MAME 输入后端审计（阶段十五）

**日期**：2026-10-14

## 任务 A：输入后端确定

| 项目 | 值 | 证据 |
|------|-----|------|
| MAME 版本 | 0.285 | `mame -version` |
| OSD 层 | SDL | 源码 src/osd/modules/input/input_sdl.cpp |
| 显示 | Xvfb :99 | 测试环境 |
| 输入路径 | SDL → X11 → Xvfb | 源码+环境推断 |

**已直接验证**：
- MAME 0.285 使用 SDL 输入模块
- 测试环境为 Xvfb :99

**源码支持但未运行时验证**：
- SDL 在 Xvfb 下使用 X11 后端（SDL 文档行为）

**推断**：
- xdotool XTest 事件 → Xvfb → SDL X11 → MAME

**未知**：
- SDL 是否过滤 synthetic 事件
- MAME 窗口焦点需求细节

## 任务 B：输入处理链路（源码）

```
X11 KeyPress
  → SDL_PollEvent
  → input_sdl.cpp
  → MAME input_seq
  → ioport_manager
  → 驱动 PORT_BIT
```

**已定位**：
- src/osd/modules/input/input_sdl.cpp（SDL 输入）
- src/emu/ioport.cpp（端口管理）
- src/mame/igs/igs017.cpp:3858（驱动定义）

**未知**：
- SDL synthetic 事件处理细节
- 焦点丢失时的行为

## 任务 C：输入配置

**独立测试实例**：
- CFG 目录：/tmp/xvfb-test/bet002/config（空）
- 无自定义输入映射
- 使用 MAME 默认

**未发现**：
- 多进程共用 DISPLAY 冲突
- 窗口目标错误

## 结论

**已直接验证**：MAME 0.285 + SDL + Xvfb 环境  
**源码支持**：输入链路代码位置已定位  
**未知**：SDL 对 synthetic 事件的处理、焦点细节
