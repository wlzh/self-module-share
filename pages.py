"""
Qwen-Image-2512 Studio (最终完美版)
适配环境：Gradio 6.2.0 + Diffusers
功能：
1. 包含下载按钮、复制参数按钮
2. 修复所有 API 过时警告
3. 极致显存优化 (24G/48G 均可运行)
"""

import gradio as gr
import torch
from diffusers import DiffusionPipeline
import gc
import random

# ================= 配置区域 =================
MODEL_PATH = "./checkpoints/Qwen-Image-2512"

# 预设宽高比
ASPECT_RATIOS = {
    "16:9 宽屏 (1664×928) - 电影感": (1664, 928),
    "9:16 竖屏 (928×1664) - 手机壁纸": (928, 1664),
    "1:1 方形 (1328×1328) - 社交头像": (1328, 1328),
    "4:3 标准 (1472×1104) - 摄影构图": (1472, 1104),
    "3:4 纵向 (1104×1472) - 海报设计": (1104, 1472),
}

DEFAULT_NEGATIVE_PROMPT = "低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，蜡像感，人脸无细节，过度光滑，画面具有AI感，构图混乱，文字模糊，扭曲，水印，文字覆盖。"

# ================= 核心逻辑 =================

pipe = None

def load_model():
    global pipe
    print("正在初始化 Qwen-Image-2512...")
    
    if torch.cuda.is_available():
        torch_dtype = torch.bfloat16
        print(f"✅ 检测到 GPU: {torch.cuda.get_device_name(0)}")
    else:
        torch_dtype = torch.float32
        print("⚠️ 未检测到 GPU，将使用 CPU")

    try:
        pipe = DiffusionPipeline.from_pretrained(
            MODEL_PATH, 
            torch_dtype=torch_dtype,
            use_safetensors=True
        )
