#!/usr/bin/env python3
"""
麻将牌面人工标注工具
用法: python3 tools/label_tiles.py --crops outputs/crops --output datasets/manifests/tile-labels.jsonl
"""
import argparse
import json
import os
from datetime import datetime

# 临时类别表（可扩展）
TILE_CLASSES = [
    "UNKNOWN_TILE",
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",  # 万
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",  # 筒
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",  # 索
    "E", "S", "W", "N",  # 风
    "Wh", "G", "R",  # 三元
    "OCCLUDED", "BLURRY", "CROP_ERROR"
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--crops', required=True, help='Tile crops directory')
    parser.add_argument('--output', required=True, help='Output JSONL path')
    args = parser.parse_args()
    
    crops = sorted([f for f in os.listdir(args.crops) if f.endswith('.png')])
    print(f"Found {len(crops)} crops")
    print(f"Classes: {', '.join(TILE_CLASSES[:10])}...")
    print("\nManual labeling required. This tool lists crops for external labeling.")
    print("Output format: JSONL with sample_id, crop_path, label, status")
    
    # 生成待标注清单
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        for crop in crops:
            sample_id = os.path.splitext(crop)[0]
            record = {
                "sample_id": sample_id,
                "crop_path": os.path.join(args.crops, crop),
                "label": "UNKNOWN_TILE",
                "status": "pending",
                "annotated_at": None,
                "notes": ""
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    
    print(f"Manifest created: {args.output}")
    print("Please label manually and update the 'label' and 'status' fields.")

if __name__ == "__main__":
    main()
