"""CreditLedger：积分流水（不可覆盖）"""
import sqlite3
import uuid
from datetime import datetime

class CreditLedger:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def record(self, game_id, amount, category, balance_after, notes=""):
        conn = sqlite3.connect(self.db_path)
        event_id = str(uuid.uuid4())[:8]
        conn.execute(
            "INSERT INTO credit_ledger (event_id, game_id, timestamp, amount, category, balance_after, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (event_id, game_id, datetime.now().isoformat(), amount, category, balance_after, notes)
        )
        conn.commit()
        conn.close()
        return event_id
    
    def get_balance(self, game_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "SELECT balance_after FROM credit_ledger WHERE game_id=? ORDER BY timestamp DESC LIMIT 1",
            (game_id,)
        )
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None
    
    def verify(self, game_id, initial_credit):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "SELECT SUM(amount) FROM credit_ledger WHERE game_id=?", (game_id,)
        )
        total_change = cur.fetchone()[0]
        final = self.get_balance(game_id)
        conn.close()
        if total_change is None:
            return (False, "No records")
        expected = initial_credit + total_change
        if expected == final:
            return (True, "OK")
        return (False, f"Expected {expected}, got {final}")
