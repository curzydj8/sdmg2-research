"""视觉识别流水线"""
import json
import os
import sys
import hashlib
from datetime import datetime

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vision.capture_loader import load_screenshot, get_image_info
from vision.state_classifier import classify_state
from vision.hand_region import detect_hand_region
from vision.tile_detector import detect_tiles
from vision.tile_classifier import classify_tile
from vision.consistency_check import check_consistency

def file_sha256(path):
    """计算文件 SHA-256"""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def run_pipeline(input_path, output_dir):
    """运行完整流水线"""
    os.makedirs(f"{output_dir}/json", exist_ok=True)
    os.makedirs(f"{output_dir}/overlays", exist_ok=True)
    os.makedirs(f"{output_dir}/reports", exist_ok=True)
    os.makedirs(f"{output_dir}/crops", exist_ok=True)
    
    # 计算原图哈希
    src_sha = file_sha256(input_path)
    
    # 1. 加载
    img = load_screenshot(input_path)
    info = get_image_info(img)
    
    # 2. 状态分类
    state_result = classify_state(input_path)
    
    basename = os.path.splitext(os.path.basename(input_path))[0]
    
    result = {
        "input": input_path,
        "source_sha256": src_sha,
        "timestamp": datetime.now().isoformat(),
        "image_info": info,
        "state": state_result,
        "tiles": [],
        "consistency": None
    }
    
    # 3-5. 如果是主对局，检测手牌
    if state_result["state"] == "MAIN_GAME":
        hand_region = detect_hand_region(img)
        result["hand_region"] = hand_region
        
        x, y, rw, rh = hand_region["bbox"]
        hand_img = img.crop((x, y, x+rw, y+rh))
        
        tiles = detect_tiles(hand_img)
        for tile in tiles:
            tx, ty, tw, th = tile["bbox"]
            tile_img = hand_img.crop((tx, ty, tx+tw, ty+th))
            
            # 保存裁切图
            crop_filename = f"{basename}-tile-{tile['index']:02d}.png"
            crop_path = f"{output_dir}/crops/{crop_filename}"
            tile_img.save(crop_path)
            
            # 分类（占位）
            cls = classify_tile(tile_img)
            tile.update(cls)
            # 全图坐标
            tile["bbox"] = [x+tx, y+ty, tw, th]
            tile["crop_path"] = crop_path
            tile["sample_id"] = f"{basename}-{tile['index']:02d}"
        
        result["tiles"] = tiles
        result["consistency"] = check_consistency(result, (info["width"], info["height"]))
    
    # 保存 JSON
    json_path = f"{output_dir}/json/{basename}-result.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    return result, json_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', default='outputs')
    args = parser.parse_args()
    result, json_path = run_pipeline(args.input, args.output)
    print(f"Result: {json_path}")
    print(f"State: {result['state']['state']}, Tiles: {len(result['tiles'])}")
