# MAME 输入可观测性（阶段十六）

**日期**：2026-10-14

## 任务 A：证据复核

**PID 36644**：✅ 存在，命令未变（只读检查）

**阶段十五证据**：
- MAME 0.285 + SDL：✅ 已验证
- Xvfb :99：✅ 已验证
- 输入路径 SDL→X11→Xvfb：⚠️ 推断（未运行时验证 SDL 后端选择）

## 任务 B：SDL 输入链路（源码）

**文件**：src/osd/modules/input/input_sdl.cpp

**键盘事件处理**（line 587-603）：
```cpp
virtual void process_event(SDL_Event const &event) override
{
    switch (event.type)
    {
    case SDL_KEYDOWN:
        m_keyboard.state[event.key.keysym.scancode] = 0x80;
        break;
    case SDL_KEYUP:
        m_keyboard.state[event.key.keysym.scancode] = 0x00;
        break;
    }
}
```

**证据等级**：
- ✅ 源码直接证实：SDL_KEYDOWN/UP 更新键盘状态数组
- ❌ 未知：SDL 是否区分 XTest synthetic 事件
- ❌ 未知：焦点变化时的行为（需查 SDL_WINDOWEVENT）

**输入到 ioport**：
- m_keyboard.state → MAME input_seq → ioport_manager
- 具体转换代码：未定位（需进一步审计）

## 任务 C：零游戏操作可观测方案

### 方案 1：静态源码审计

- **能证明**：代码路径存在
- **不能证明**：运行时实际行为
- **工具**：curl + grep
- **副作用**：无

### 方案 2：日志/调试输出

- **检查**：MAME -verbose 是否记录输入事件
- **结果**：❌ 未找到输入事件日志选项（源码中无）
- **副作用**：无

### 方案 3：独立 SDL 测试程序

- **能证明**：SDL/X11 一般事件路径
- **不能证明**：MAME 实例实际接收
- **工具**：xev（已用，阶段十四）
- **副作用**：无（不运行 MAME）

### 方案 4：确认 MAME SDL 事件循环

- **方法**：无（无观察接口）
- **副作用**：N/A

## 任务 D：结论

**B**：只能验证 SDL/X11 的一般事件路径，无法证明 MAME 实例的实际接收。

**理由**：
1. xev 证明 X11 事件可投递（需焦点）
2. 源码证明 MAME 有 SDL 事件处理代码
3. 但无方法观察特定 MAME 进程的 SDL 事件循环
4. MAME 不记录输入事件到日志

## 授权申请

**结论 C**：必须经过受控的真实游戏按键测试，才能验证端到端链路。

详见 MAME-INPUT-TEST-AUTHORIZATION-REQUEST.md（如需）。
