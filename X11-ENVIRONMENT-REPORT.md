# X11 环境评估报告

**日期**：2026-10-14

## 当前状态

| 项目 | 结果 |
|------|------|
| 会话类型 | Wayland |
| 显示管理器 | gdm3（运行中） |
| X11 会话 | ❌ 未安装（/usr/share/xsessions/ 不存在） |
| Xorg | ❌ 未安装 |

## 安装 X11 所需

```bash
sudo apt update
sudo apt install -y xorg gnome-session-x11
```

预计下载约 200-300MB，安装后 `/usr/share/xsessions/` 会出现 `gnome-xorg.desktop`。

## 切换步骤（需用户在登录界面操作）

1. 在当前桌面注销（右上角 → 注销）
2. 在 GDM 登录界面，点击用户名
3. 点击右下角齿轮图标 ⚙️
4. 选择 **"GNOME on Xorg"**（不是默认的 "GNOME"）
5. 输入密码登录

## 风险

- 注销会关闭所有图形应用（包括 MAME）
- SSH 不受影响（独立通道）
- 可随时注销切回 Wayland（选 "GNOME"）

## 恢复方案

- 切回 Wayland：注销 → 齿轮 → 选 "GNOME" → 登录
- 卸载 X11：`sudo apt remove xorg gnome-session-x11`（不建议，影响不大可保留）

## 结论

X11 可安装，但**切换必须用户在登录界面手动选择**，无法远程无感切换。
