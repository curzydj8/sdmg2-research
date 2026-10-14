#!/usr/bin/env python3
"""
视觉样本管理工具
用法: python3 tools/dataset_audit.py --index GAME-STATE-CLASSIFIER-DATASET-INDEX.json
"""
import argparse
import json
import os
import hashlib
from PIL import Image

ALLOWED_LABELS = ["MAIN_GAME", "REWARD", "ODDS", "TITLE", "UNKNOWN_STATE"]

def audit_dataset(index_path):
    with open(index_path) as f:
        dataset = json.load(f)
    
    print(f"样本总数: {len(dataset)}")
    for s in dataset:
        path = s["path"]
        # 验证文件
        if not os.path.exists(path):
            print(f"❌ 缺失: {path}")
            continue
        # 验证 SHA
        with open(path, 'rb') as f:
            sha = hashlib.sha256(f.read()).hexdigest()[:16]
        sha_ok = sha == s["sha256_prefix"]
        # 验证标签
        label_ok = s["label"] in ALLOWED_LABELS
        # 验证尺寸
        img = Image.open(path)
        print(f"{'✅' if sha_ok and label_ok else '❌'} {s['label']}: {path} ({img.size[0]}x{img.size[1]})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', required=True)
    args = parser.parse_args()
    audit_dataset(args.index)
