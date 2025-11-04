import torch

MODEL_PATH = "model/chest-x-raydense.pth"
STATIC_DIR = "static/images"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
IMAGE_SIZE = 224