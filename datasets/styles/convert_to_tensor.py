# convert_to_tensor.py
import torch
from PIL import Image
from torchvision import transforms

def image_to_tensor(path):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5])
    ])
    img = Image.open(path).convert("RGB")
    return transform(img)
