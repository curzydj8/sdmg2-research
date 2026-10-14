# Bet 隔离测试环境报告

**日期**：2026-10-14

## 原实例状态

- **PID 36644**：运行中（只读检查，未发送信号）
- **命令**：mame sdmg2754ca -rompath /home/zhangdawei/roms -window
- **状态**：未触碰

## 测试环境

**目录**：~/workspace/sdmg2-test/experiments/bet-mapping-002/
- config/：独立 MAME 配置
- nvram/：独立 NVRAM（空白）
- screenshots/：截图
- logs/：日志

**隔离确认**：
- ✅ 配置目录：独立，不使用 ~/.mame/cfg/
- ✅ NVRAM 目录：独立，不使用 ~/.mame/nvram/
- ✅ 不会写入原实例文件

## 启动命令（待执行）

```
mame sdmg2754ca \
  -rompath /home/zhangdawei/roms \
  -window \
  -cfg_directory ~/workspace/sdmg2-test/experiments/bet-mapping-002/config \
  -nvram_directory ~/workspace/sdmg2-test/experiments/bet-mapping-002/nvram
```

**MAME 版本**：0.285  
**ROM**：sdmg2754ca  
**驱动**：igs017.cpp

## 安全状态

- ✅ 原实例未触碰
- ✅ 目录隔离已确认
- ✅ 可安全启动独立实例
