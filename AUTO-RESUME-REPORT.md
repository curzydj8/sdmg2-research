# 自主游戏恢复报告

**日期**：2026-10-14

## 实例退出原因

**MAME 实例**（PID 77327）：
- 退出时状态：ODDS，CREDIT=50，BET=0
- 原因：无法下注，脚本持续按 "5" 累积积分，实例最终退出
- 日志：mame.log 为空，无崩溃信息
- 截图：91 张已保留

**脚本**（auto_play.py）：
- 运行 01:18:32
- 因 MAME 退出而空转，已停止

## 恢复尝试

**新实例**（PID 114686）：
- 配置：Joystick 模式（DIP DSW2 mask 64 value 0）
- 状态：成功启动，TITLE → ODDS，CREDIT=2
- Bet 测试：Alt_L, x, z, space 均无效（BET=0）

## 阻塞原因

1. **DIP 配置可能未生效**：cfg 文件格式或加载问题
2. **或按键映射仍错误**：Joystick 模式下 BUTTON2 的键盘映射未知

## 数据保留

- ✅ 91 张截图（/tmp/xvfb-test/auto/screenshots/）
- ✅ 配置文件
- ✅ 日志（空）

## 安全

- ✅ PID 36644 存活，未受影响
- ✅ SSH 正常
- ✅ 测试实例已清理

## 下一步

需验证 DIP 配置是否真正生效，或查找 Mahjong 模式下的下注按键。
