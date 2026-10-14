"""GameSessionRecorder：真实牌局记录器"""
from dataclasses import dataclass, field
from typing import List, Optional
import uuid
import json
import os
from datetime import datetime

@dataclass
class GameAction:
    pre_state: str
    action: str
    post_state: str
    credit_before: int
    credit_after: int
    screenshot_hash: str

class GameSessionRecorder:
    """牌局记录器（真实/模拟/测试分开）"""
    
    def __init__(self, data_dir="learning/sessions"):
        self.data_dir = data_dir
        os.makedirs(f"{data_dir}/real", exist_ok=True)
        os.makedirs(f"{data_dir}/simulation", exist_ok=True)
        os.makedirs(f"{data_dir}/test", exist_ok=True)
    
    def start_session(self, session_type="real") -> str:
        """开始新会话"""
        assert session_type in ["real", "simulation", "test"]
        sid = f"{session_type}_{uuid.uuid4().hex[:8]}"
        return sid
    
    def record_action(self, session_id, action: GameAction):
        """记录动作"""
        session_type = session_id.split("_")[0]
        path = f"{self.data_dir}/{session_type}/{session_id}.jsonl"
        with open(path, "a") as f:
            f.write(json.dumps(action.__dict__, ensure_ascii=False) + "\n")
