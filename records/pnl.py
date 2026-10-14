"""盈亏统计模块"""
import sqlite3

class PnLStats:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def compute(self):
        """计算统计指标"""
        conn = sqlite3.connect(self.db_path)
        
        # 已结算牌局
        cur = conn.execute("SELECT COUNT(*) FROM game_rounds WHERE settled=1")
        settled = cur.fetchone()[0]
        
        # 胜/负/平
        cur = conn.execute("SELECT result, COUNT(*) FROM game_rounds WHERE settled=1 GROUP BY result")
        results = dict(cur.fetchall())
        wins = results.get("WIN", 0)
        losses = results.get("LOSS", 0)
        draws = results.get("DRAW", 0)
        
        # 累计上分、投入、返还
        cur = conn.execute("SELECT SUM(amount) FROM credit_ledger WHERE category='TOP_UP'")
        top_up = cur.fetchone()[0] or 0
        
        cur = conn.execute("SELECT SUM(amount) FROM credit_ledger WHERE amount < 0")
        invested = abs(cur.fetchone()[0] or 0)
        
        cur = conn.execute("SELECT SUM(amount) FROM credit_ledger WHERE amount > 0 AND category != 'TOP_UP'")
        returned = cur.fetchone()[0] or 0
        
        conn.close()
        
        net = returned - invested
        total_games = wins + losses + draws
        
        return {
            "settled_rounds": settled,
            "wins": wins,
            "losses": losses,
            "draws": draws,
            "win_rate": wins / total_games if total_games > 0 else "UNKNOWN",
            "total_top_up": top_up,
            "total_invested": invested,
            "total_returned": returned,
            "net_pnl": net,
            "avg_per_round": net / total_games if total_games > 0 else "UNKNOWN",
            # 收益率分母：累计投入
            "roi": net / invested if invested > 0 else "UNKNOWN",
            "roi_denominator": "total_invested",
        }
