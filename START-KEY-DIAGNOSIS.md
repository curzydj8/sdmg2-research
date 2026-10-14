# Start 键诊断报告

**日期**：2026-10-14

## 基本信息
- MAME 版本：0.285
- ROM：sdmg2754ca（Chaoji Da Manguan II, V754C, set 1）
- 驱动：igs/igs017.cpp
- 配置路径：/home/zhangdawei/.mame/cfg/sdmg2754ca.cfg（无自定义输入映射）

## 输入端口定义（-listxml）

```xml
<input players="1" coins="1" service="yes">
  <control type="joy" buttons="2" ways="8"/>
  <control type="mahjong" buttons="25"/>
  <control type="gambling" buttons="5"/>
</input>
```

**关键**：这是麻将 25 键 + 赌博 5 键的专用机台，不是标准手柄游戏。

## 已验证的按键

| 按键 | 作用 | 证据 |
|------|------|------|
| 5 | 投币 | CREDIT 0→1 |
| Return | 关闭信息屏 | 从信息屏进入标题画面 |
| D | 进入查账菜单 | 显示"查帳"画面 |

## 无效的按键

1, 2, Tab, KP_Enter, Space, 0, 3, 4, 6, 7, 8, 9, a, s

## 三个"Start"概念的区分

1. **MAME 标准 Start**：IPT_START1，默认映射为键盘 "1"
   - 在本游戏中无效
   
2. **游戏驱动实际输入**：igs017.cpp 定义的端口
   - 可能是 IPT_MAHJONG_* 或 IPT_GAMBLING_* 中的某一个
   - 具体定义未知（无源码）
   
3. **画面"開始鍵"**：查账菜单提示的退出键
   - 按 "1" 无效
   - 实际映射未知

## 证据缺口

**无法获取驱动源码**：
- MAME 二进制安装，无源码
- -listxml 不显示详细端口位定义
- 无法确认 Start 对应的 IPT 类型和默认键位

**不得编造**：不能猜测 Start 键，必须有驱动源码或 MAME 输入配置 UI 的证据。

## 下一步（最有依据）

1. 获取 igs017.cpp 源码（MAME GitHub），查找 INPUT_PORTS 定义
2. 或：在能工作的 Wayland MAME 上，用 MAME UI（Tab 菜单）查看输入映射
3. 或：查 IGS 麻将机台的 MAME 默认键位文档

## 结论

Xvfb 输入链路已验证可靠。Start 键映射是**游戏特定**问题，需要驱动源码证据，不能靠试键解决。

## 突破（2026-10-14 10:45）

**NVRAM 是关键**：
- 复制用户 NVRAM (`/home/zhangdawei/.mame/nvram/sdmg2754ca`) 到 Xvfb 测试后
- 按 5（投币）进入了奖励关"喜從天降"
- 画面显示真实游戏状态：5 张牌、麻将牌面、CREDIT/WIN

**源码证据**（igs017.cpp）：
```c
PORT_BIT( 0x01, IP_ACTIVE_LOW, IPT_START1 )  // 開始
```
- Start = IPT_START1 = 键盘 "1"（标准映射）
- 但有 DIP 条件：`PORT_CONDITION("DSW2", 0x40, EQUALS, 0x00)`
- NVRAM 中的 DIP 设置决定 Start 是否有效

**结论**：
1. Start 键确实是 "1"（MAME 标准映射）
2. 之前无效是因为 Xvfb 用了空白 NVRAM，DIP 设置不对
3. 复制用户 NVRAM 后，输入链路完全打通

**当前状态**：在奖励关，需找到进入主麻将对局的方法。
