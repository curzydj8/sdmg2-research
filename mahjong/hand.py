"""手牌数据结构"""
from .tile import is_valid_code

class Hand:
    def __init__(self, tiles=None):
        self.tiles = []
        if tiles:
            for t in tiles:
                self.add(t)
    
    def add(self, tile_code):
        """添加一张牌"""
        if not is_valid_code(tile_code):
            raise ValueError(f"Invalid tile code: {tile_code}")
        if tile_code != -1 and self.tiles.count(tile_code) >= 4:
            raise ValueError(f"Tile {tile_code} exceeds 4 copies")
        self.tiles.append(tile_code)
    
    def count(self):
        return len(self.tiles)
    
    def validate(self):
        """验证手牌合法性"""
        if len(self.tiles) > 14:
            return False, "Too many tiles"
        for t in self.tiles:
            if not is_valid_code(t):
                return False, f"Invalid tile: {t}"
            if t != -1 and self.tiles.count(t) > 4:
                return False, f"Tile {t} exceeds 4"
        return True, "OK"
