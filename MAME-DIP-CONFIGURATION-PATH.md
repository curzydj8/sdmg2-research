# MAME DIP 配置路径

**日期**：2026-10-14  
**MAME 版本**：0.285

## 官方 DIP 设置方法

### 1. MAME UI（Tab 菜单）
- 路径：Tab → Dip Switches
- 状态：**无法使用**（Tab 无反应，原因未明）
- 证据：MAME-UI-DIAGNOSIS-REPORT.md

### 2. 配置文件（.cfg）
- 位置：~/.mame/cfg/sdmg2754ca.cfg
- 格式：XML，可含 <dipswitch> 或 <input> 节点
- 实际内容：无 DIP 设置（20 行，仅系统设置）
- 状态：**未设置**

### 3. 命令行
- 检查：mame -showusage 无 DIP 相关选项
- 状态：**不支持**

## 结论

**官方途径均不可用或未使用**：
- UI 打不开
- cfg 未设置
- 命令行不支持

**DIP 实际值来源不明**，与"存储位置尚未确认"一致。
