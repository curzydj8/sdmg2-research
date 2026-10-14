# 演示模式选项

**日期**：2026-10-14  
**驱动**：igs017.cpp, sdmg2

## DIP 开关检查

### Demo_Sounds (SW1:8)
- **位置**：igs017.cpp:3802
- **定义**：
  ```
  PORT_DIPNAME( 0x80, 0x80, DEF_STR( Demo_Sounds ) )
    PORT_DIPSETTING( 0x00, Off )
    PORT_DIPSETTING( 0x80, On )
  ```
- **功能**：仅控制演示音乐开关
- **验证状态**：未验证
- **风险**：低（仅声音）
- **结论**：不能关闭演示画面循环

### Demo Game (SW2:6)
- **状态**：sdmg2 无此 DIP（其他游戏有）
- **结论**：不适用

## 服务/测试模式

### Service (测试)
- **位置**：igs017.cpp:3711
- **定义**：`PORT_SERVICE_NO_TOGGLE( 0x04, IP_ACTIVE_LOW )` // 测试（开机时按住进入输入测试）
- **功能**：输入测试，非游戏模式切换
- **验证状态**：未验证
- **风险**：中（可能进入测试菜单）

## 结论

**无现成开关可关闭演示循环**：
- Demo_Sounds 仅关声音
- Service 仅做输入测试
- 无 Demo Game DIP

**演示循环 likely 硬编码在 ROM 中**，需静态分析定位。
