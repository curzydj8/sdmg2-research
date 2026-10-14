# MAME 版本与驱动审计

**日期**：2026-10-14

## 运行实例

| 项目 | 值 | 来源 |
|------|-----|------|
| PID | 36644 | ps |
| 命令 | mame sdmg2754ca -rompath /home/zhangdawei/roms -window | /proc/36644/cmdline |
| 可执行文件 | /usr/games/mame | which mame |
| 版本 | 0.285 | mame -version |
| ROM | sdmg2754ca | 命令行 |
| 驱动 | igs017.cpp（推断） | 游戏信息屏显示 "Source file: igs/igs017.cpp" |

## 源码版本

| 项目 | 值 |
|------|-----|
| 核对源码 | mame0285 标签（GitHub） |
| DIP 定义 | 一致（0x40=Mahjong 默认） |
| Start 条件 | 一致（仅 Joystick 模式有效） |

**结论**：运行版本与源码版本匹配，无版本差异问题。

## 证据等级

- **源码确认**：DIP 定义、默认值、Start 条件
- **运行时实测**：PID、命令行、版本、游戏行为
- **合理推断**：驱动为 igs017.cpp（基于游戏信息屏）
- **仍未知**：DIP 实际存储位置、用户 NVRAM 为何是 Joystick 模式
