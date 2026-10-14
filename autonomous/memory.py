"""ExperienceMemory：经验记录"""
from dataclasses import dataclass, field
from typing import List, Optional
import json
import os

@dataclass
class ExperienceRecord:
    session_id: str
    env_id: str
    game_state: str
    screenshot_sha_before: str
    screenshot_sha_after: str = ""
    known_vars: dict = field(default_factory=dict)
    action: str = ""
    auth_basis: str = ""
    expected: str = ""
    actual: str = ""
    failure_reason: str = ""
    repeatable: Optional[bool] = None
    next_suggestion: str = ""

class ExperienceMemory:
    """经验记录：保留成功和失败，不覆盖"""
    
    def __init__(self, store_path="autonomous/experience.jsonl"):
        self.store_path = store_path
    
    def record(self, rec: ExperienceRecord):
        os.makedirs(os.path.dirname(self.store_path) or ".", exist_ok=True)
        with open(self.store_path, "a") as f:
            f.write(json.dumps(rec.__dict__, ensure_ascii=False) + "\n")
    
    def get_all(self):
        if not os.path.exists(self.store_path):
            return []
        with open(self.store_path) as f:
            return [json.loads(line) for line in f if line.strip()]
