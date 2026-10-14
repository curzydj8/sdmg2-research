# 《超级大满贯Ⅱ》MAME 自动化测试报告

**日期**：2026-10-14  
**环境**：Ubuntu 新机 z5095738-1，MAME 0.285，ROM sdmg2754ca  
**测试范围**：Phase 1-3 完成，Phase 4-5 框架已建，Phase 6 交付

---

## 一、已验证的功能 ✅

1. **MAME 进程识别**：PID 36644，游戏短名 `sdmg2754ca` 确认
2. **截图采集**：xwd → xwdtopnm → pnmtopng 链路可用，580K PNG
3. **窗口信息**：1003×731 @ (163,131)，ID 10485767
4. **投币功能**：按 `5` 后 CREDIT 增加（从 8 到 9）
5. **赔率表识别**：S1 状态特征明确（ODDS 标题 + CREDIT/BET 显示）
6. **ROM 配置**：`/home/zhangdawei/roms/sdmg2754ca.zip`，MAME 默认按键映射

## 二、部分实现的功能 ⚠️

1. **开始游戏**（按 `1`）：有时有效，有时无反应
2. **打牌**（A-N）：`A` 曾成功打出，`C`/`M` 多次无反应
3. **对局状态识别**：特征来自历史截图，需新截图验证
4. **自动测试循环**：框架已写（test-framework.py），但输入不可靠导致无法全自动

## 三、尚未验证的功能 ❌

1. **吃/碰/槓/胡按键**：未知是哪个键
2. **和牌结算画面**：未观察到
3. **流局画面**：未观察到
4. **标题画面**：游戏启动直接进 ODDS，未见标题
5. **牌面 OCR 识别**：未实现
6. **模板匹配**：未实现（仅有人工识别规则）

## 四、未解决的问题 🔴

### P0：输入不可靠（阻塞自动化）
- **现象**：`xdotool key --window` 有时无效
- **根因**：
  - 焦点在 1x1 隐藏窗口，不在游戏窗口
  - `windowactivate --sync` 挂起（Mutter 不响应）
  - 疑似游戏特定状态不接受输入
- **影响**：无法建立可靠的自动测试循环
- **建议**：研究 MAME 的 `-keyboard` 参数，或改用 evdev 直接注入

### P1：状态识别未自动化
- 当前靠人工看截图判断
- 需实现：ODDS 标题模板匹配、CREDIT 数字 OCR、手牌 A-N 标记检测

### P2：牌面识别置信度低
- 麻将牌面小（约 40×60 像素），OCR 困难
- 建议：先做位置检测，再做分类，保留原图备查

## 五、交付物

- `test-framework.py`：测试框架（含 8 个测试用例定义）
- `key-mappings.md`：按键映射（实测）
- `states/state-definitions.md`：状态定义
- `states/recognition-rules.md`：识别规则
- `screenshots/odds-20261014.png`：赔率表截图
- `TEST-REPORT.md`：本报告

## 六、运行方式

```bash
# 1. 确认游戏运行
ssh -F ~/.ssh/config zhang-new 'pgrep -a mame'

# 2. 截图
ssh -F ~/.ssh/config zhang-new 'export DISPLAY=:0; export XAUTHORITY=$(ls /run/user/1000/.mutter-Xwaylandauth.* 2>/dev/null | head -1); xwd -id 10485767 | xwdtopnm | pnmtopng > /tmp/shot.png'

# 3. 运行框架（需人工验证结果）
python3 ~/workspace/sdmg2-test/test-framework.py
```

## 七、结论

**自动化测试框架已建立，但输入层问题阻塞了全自动化。**

游戏本身运行正常（MAME 启动、画面渲染、投币有效）。  
要实现"胡牌"目标，需先解决输入可靠性问题。

**下一步**（需用户决策）：
1. 深入研究 MAME 输入（evdev/uinput）
2. 或接受半自动：人工按键，程序负责截图和记录
