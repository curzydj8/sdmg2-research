#!/usr/bin/env python3
"""
模板构建器：从真实游戏截图裁剪牌面模板
用法：python3 template_builder.py <screenshot> <tile_name> <x> <y> <w> <h>
"""
import cv2
import sys
import os

def build_template(screenshot_path, tile_name, x, y, w, h):
    img = cv2.imread(screenshot_path)
    if img is None:
        print(f"无法读取 {screenshot_path}")
        return False
    
    # 裁剪
    tile = img[y:y+h, x:x+w]
    
    # 转灰度（模板匹配用灰度）
    gray = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY)
    
    # 保存
    out_dir = os.path.expanduser("~/workspace/sdmg2-test/templates")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{tile_name}.png")
    cv2.imwrite(out_path, gray)
    print(f"模板已保存: {out_path} ({w}x{h})")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("用法: python3 template_builder.py <截图> <牌名> <x> <y> <w> <h>")
        print("示例: python3 template_builder.py screenshots/gameplay-20261014.png wan1 30 580 65 90")
        sys.exit(1)
    
    build_template(sys.argv[1], sys.argv[2], 
                   int(sys.argv[3]), int(sys.argv[4]), 
                   int(sys.argv[5]), int(sys.argv[6]))
