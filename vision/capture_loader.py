"""截图加载器"""
from PIL import Image
import os

def load_screenshot(path):
    """加载截图为 PIL Image"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Screenshot not found: {path}")
    return Image.open(path).convert('RGB')

def get_image_info(img):
    """获取图像基本信息"""
    w, h = img.size
    return {"width": w, "height": h, "mode": img.mode}
