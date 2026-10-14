#!/usr/bin/env python3
"""
游戏控制器 v1.0
闭环：截图 → 识别 → 决策 → 执行 → 验证 → 记录
"""
import time, json
from datetime import datetime

class GameController:
    def __init__(self, input_adapter, screen_reader, state_detector, strategy, executor, recovery):
        self.input = input_adapter
        self.screen = screen_reader
        self.detector = state_detector
        self.strategy = strategy
        self.executor = executor
        self.recovery = recovery
        self.history = []
    
    def log(self, entry):
        entry["timestamp"] = datetime.now().isoformat()
        self.history.append(entry)
        print(f"[{entry['timestamp'][11:19]}] {entry.get('event','')} {entry.get('detail','')}", flush=True)
    
    def run_one_action(self, action):
        """执行单个动作并记录"""
        result = self.executor.execute(action, verify=True)
        success = result.get("success", False)
        
        self.log({"event": "action", "detail": f"{action} -> {result}",
                  "success": success})
        
        if not self.recovery.record(success):
            self.log({"event": "STOP", "detail": "连续失败达阈值，停止"})
            return False
        return True
    
    def ensure_coins_and_start(self):
        """投币并开始（如果当前在ODDS界面）"""
        img, msg = self.screen.capture()
        if img is None:
            self.log({"event": "error", "detail": f"截图失败: {msg}"})
            return False
        state, conf, _ = self.detector.detect(img)
        self.log({"event": "state", "detail": f"{state} (conf={conf:.2f})"})
        
        if state == "ODDS":
            # 投币
            if not self.run_one_action(("coin",)):
                return False
            time.sleep(1)
            # 开始
            if not self.run_one_action(("start",)):
                return False
            return True
        elif state == "GAMEPLAY":
            self.log({"event": "info", "detail": "已在对局中"})
            return True
        else:
            self.log({"event": "error", "detail": f"未知状态 {state}，不操作"})
            return False
    
    def save_history(self, path):
        with open(path, "w") as f:
            json.dump(self.history, f, indent=1, ensure_ascii=False)
