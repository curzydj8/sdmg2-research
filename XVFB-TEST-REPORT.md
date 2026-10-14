# Xvfb 隔离测试报告

**日期**：2026-10-14  
**显示**：:99 (1280x800)  
**MAME PID**：58964（Xvfb），36644（原 Wayland 实例未动）

## 测试结果

| 项目 | 结果 |
|------|------|
| MAME 在 Xvfb 启动 | ✅ 正常，显示目标游戏 |
| 虚拟显示截图 | ✅ 真实游戏画面 |
| xdotool 按键到达 | ✅ Return/5/D 均生效 |
| 投币（5） | ✅ CREDIT 0→1（硬证据） |
| 开始键（1） | ❌ 未进入对局 |
| Tab 菜单 | ❌ 无反应 |

## 关键发现

1. **Xvfb 方案可行**：纯 X11 环境下 xdotool 可靠工作
2. **输入链路通**：`windowactivate`（不带 --sync）+ `key`（不带 --window）是正确用法
3. **Start 键映射问题**：游戏是麻将专用机台，Start 不是标准 "1" 键
   - 按 D 进入查账菜单，证明输入能到游戏
   - 查账菜单要求按"開始鍵"退出，但 1 键无效
   - 需查明该游戏的 Start 实际映射

## 证据

- screenshots/xvfb-game1.png：MAME 信息屏
- screenshots/xvfb-game3.png：标题画面（Return 生效）
- screenshots/xvfb-game4.png：ODDS，CREDIT 1（投币生效）
- screenshots/xvfb-game9.png：查账菜单（D 键生效）

## 清理

- Xvfb :99（PID 57319）：保留（测试用）
- MAME Xvfb（PID 58964）：保留（测试用）
- 原 MAME（PID 36644）：未动

## 下一步

1. 查明 sdmg2754ca 的 Start 键实际映射（MAME 驱动输入定义）
2. 用正确按键进入对局
3. 验证麻将牌面识别
4. 开始自动打牌

## 结论

**Xvfb 方案验证通过**。输入链路在纯 X11 下可靠。剩余问题是游戏特定的按键映射，不是基础设施问题。
