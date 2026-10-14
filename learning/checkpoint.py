"""检查点与断点续跑"""
import json
import os
from datetime import datetime

class CheckpointManager:
    def __init__(self, path="learning/checkpoints.json"):
        self.path = path
        self.data = self._load()
    
    def _load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {
            "tasks_completed": [],
            "tasks_pending": ["Q-001", "Q-002", "Q-003"],
            "rules_verified": ["R-001", "R-002"],
            "last_state": None,
            "mame_restarts": 0,
            "action_failures": 0,
        }
    
    def save(self):
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        self.data["last_saved"] = datetime.now().isoformat()
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def complete_task(self, task_id):
        if task_id in self.data["tasks_pending"]:
            self.data["tasks_pending"].remove(task_id)
        if task_id not in self.data["tasks_completed"]:
            self.data["tasks_completed"].append(task_id)
        self.save()
    
    def record_mame_exit(self, pid, reason):
        self.data["mame_restarts"] += 1
        self.data["last_exit"] = {"pid": pid, "reason": reason, "time": datetime.now().isoformat()}
        self.save()
