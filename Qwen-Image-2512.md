# 告别“AI脸”与文字乱码！阿里 2025 年 12 月 31 日开源模型Qwen-Image-2512，本地部署全攻略 🔥

## 安装指南


### 创建运行环境

conda create -n qwenimage python=3.10 -y conda activate qwenimage

### 克隆项目

 mkdir qwenimage cd qwenimage

### 安装依赖组件

pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124 pip install git+https://github.com/huggingface/diffusers pip install transformers gradio accelerate

### 模型下载

#### 如果网络没问题
hf download Qwen/Qwen-Image-2512 --local-dir checkpoints/Qwen-Image-2512

#### 如果huggingface连不上，用下面这个命令

modelscope download --model Qwen/Qwen-Image-2512 --local_dir checkpoints/Qwen-Image-2512

### 推理演示

python pages.py
