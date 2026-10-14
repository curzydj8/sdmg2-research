#!/usr/bin/env python3
"""错误恢复管理器 v1.0"""
import time

class RecoveryManager:
    def __init__(self, max_retries=3, fail_threshold=5):
        self.max_retries = max_retries
        self.fail_threshold = fail_threshold
        self.consecutive_failures = 0
        self.stopped = False
    
    def record(self, success):
        """记录一次操作结果"""
        if success:
            self.consecutive_failures = 0
        else:
            self.consecutive_failures += 1
        if self.consecutive_failures >= self.fail_threshold:
            self.stopped = True
            return False  # 触发停止
        return True
    
    def should_stop(self):
        return self.stopped
    
    def get_status(self):
        return {"consecutive_failures": self.consecutive_failures,
                "stopped": self.stopped,
                "threshold": self.fail_threshold}
