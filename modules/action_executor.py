#!/usr/bin/env python3
"""动作执行器 v1.0：执行动作并验证结果"""
import time

class ActionExecutor:
    def __init__(self, input_adapter, screen_reader, state_detector):
        self.input = input_adapter
        self.screen = screen_reader
        self.detector = state_detector
        self.log = []
    
    def execute(self, action, verify=True):
        """
        :param action: ('coin',) / ('start',) / ('discard', slot)
        :param verify: 是否截图验证
        :return: dict with success, before/after states, message
        """
        # 前置截图
        img_before, msg1 = self.screen.capture()
        if img_before is None:
            return {"success": False, "error": f"前置截图失败: {msg1}"}
        state_before, conf_before, _ = self.detector.detect(img_before)
        
        # 执行
        if action[0] == "coin":
            ok, msg = self.input.coin()
        elif action[0] == "start":
            ok, msg = self.input.start()
        elif action[0] == "discard":
            ok, msg = self.input.discard(action[1])
        else:
            return {"success": False, "error": f"未知动作 {action}"}
        
        if not ok:
            return {"success": False, "error": f"输入失败: {msg}",
                    "before_state": state_before}
        
        time.sleep(2.0)  # 等游戏响应
        
        # 后置验证
        if verify:
            img_after, msg2 = self.screen.capture()
            if img_after is None:
                return {"success": None, "warning": f"后置截图失败: {msg2}, 无法验证",
                        "before_state": state_before}
            state_after, conf_after, _ = self.detector.detect(img_after)
            # 简单验证：状态变化或保持（由调用者判断）
            return {"success": True, "before_state": state_before, "after_state": state_after,
                    "before_conf": conf_before, "after_conf": conf_after, "note": msg}
        return {"success": True, "note": "未验证"}
