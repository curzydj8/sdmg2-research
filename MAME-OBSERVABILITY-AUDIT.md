# MAME 可观察性审计

**日期**：2026-10-14

## 隔离环境

**存在**：✅

| 项目 | 路径 |
|------|------|
| 配置 | /tmp/xvfb-test/bet002/config |
| NVRAM | /tmp/xvfb-test/bet002/nvram |
| 截图 | /tmp/xvfb-test/bet002/screenshots |
| 日志 | /tmp/xvfb-test/bet002/logs |

**启动方式**：
```bash
DISPLAY=:99 /usr/games/mame sdmg2754ca \
  -rompath /home/zhangdawei/roms \
  -window \
  -cfg_directory /tmp/xvfb-test/bet002/config \
  -nvram_directory /tmp/xvfb-test/bet002/nvram
```

**隔离性**：✅ 与原 PID 36644 完全分离

## 输入路径

```
xdotool key 5
  → X11 XTest 事件
  → Xvfb :99
  → MAME 窗口
  → ??? (未验证)
  → 游戏逻辑
```

**验证状态**：
- ✅ 命令执行成功
- ❌ X11 事件到达未验证
- ❌ MAME 接收未验证
- ✅ 游戏响应已观察（ODDS+CREDIT 1，单次）

## 截图路径

```
xwd -id $WID
  → X11 窗口像素
  → xwdtopnm → pnmtopng
  → PNG 文件
```

**验证**：✅ 图像内容与预期一致

## 事件记录

**现有能力**：
- ✅ 时间戳（脚本记录）
- ✅ 前后截图
- ❌ 输入事件确认（无独立证据）

## 结论

**三层验证**：
1. 命令发送：✅ 可记录
2. 事件到达：❌ 未验证
3. 游戏执行：⚠️ 仅单次画面证据

不得将「按键发送成功」等同于「游戏执行动作」。
