# X11 安装报告

**日期**：2026-10-14

## 安装结果

| 项目 | 状态 |
|------|------|
| xorg | ✅ 已安装（18 个包，/usr/bin/Xorg 存在） |
| gnome-session | ✅ 已安装 |
| X11 登录会话 | ❌ **不可用** |

## 关键发现

Ubuntu 26.04 的 GNOME 已**移除 X11 会话支持**：
- `/usr/share/xsessions/` 不存在
- 只有 `/usr/share/wayland-sessions/ubuntu.desktop`
- `apt-cache search` 找不到 GNOME X11 会话包

**结论**：无法通过登录界面切换到 "GNOME on Xorg"，该选项不存在。

## 影响

原计划"切换到 X11 测试输入"不可行。Wayland 是唯一可用的 GNOME 会话。

## 替代方案

**Xvfb（虚拟 X11 显示）**：
- 不需要物理显示器，不需要切换会话
- 在虚拟的 X11 服务器中运行 MAME
- xdotool 在纯 X11 环境下可靠工作
- 不影响当前 Wayland 桌面和 SSH

```bash
sudo apt install xvfb
Xvfb :99 &
DISPLAY=:99 mame sdmg2754ca &
```

**待验证**：Xvfb 下 MAME 输入是否可靠。

## 配置变更

- 新增：xorg、gnome-session（27+1 个包）
- 删除：无
- 修改默认会话：无
- 修改 GDM 配置：无

## 下一步

需用户决策：
1. 尝试 Xvfb 虚拟显示方案
2. 或接受 Wayland 限制，寻找其他输入方案
