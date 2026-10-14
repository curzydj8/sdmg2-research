"""SQLite 数据模式"""
import sqlite3
import os

SCHEMA = """
CREATE TABLE IF NOT EXISTS game_sessions (
    session_id TEXT PRIMARY KEY,
    started_at TEXT,
    ended_at TEXT,
    top_up_amount INTEGER DEFAULT 1000,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS game_rounds (
    game_id TEXT PRIMARY KEY,
    session_id TEXT,
    started_at TEXT,
    ended_at TEXT,
    initial_credit INTEGER,
    final_credit INTEGER,
    bet_amount INTEGER,
    result TEXT,  -- WIN/LOSS/DRAW/UNKNOWN
    settled BOOLEAN DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES game_sessions(session_id)
);

CREATE TABLE IF NOT EXISTS credit_ledger (
    event_id TEXT PRIMARY KEY,
    game_id TEXT,
    timestamp TEXT,
    amount INTEGER,  -- 正=转入/返还，负=下注/投入
    category TEXT,  -- TOP_UP/BET/WIN_RETURN/DOUBLE_UP/GRAND_SLAM
    balance_after INTEGER,
    notes TEXT,
    FOREIGN KEY (game_id) REFERENCES game_rounds(game_id)
);

CREATE TABLE IF NOT EXISTS game_events (
    event_id TEXT PRIMARY KEY,
    game_id TEXT,
    timestamp TEXT,
    state TEXT,
    state_confidence REAL,
    action TEXT,
    screenshot_sha TEXT,
    FOREIGN KEY (game_id) REFERENCES game_rounds(game_id)
);
"""

def init_db(db_path):
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    conn.commit()
    return conn
