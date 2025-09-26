# preprocess_styles.py
import torchvision.transforms as T
from PIL import Image
import os

def preprocess_styles(input_dir, output_dir):
    transform = T.Compose([
        T.Resize((256, 256)),
        T.ToTensor(),
        T.Normalize([0.5], [0.5])
    ])
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        img = Image.open(os.path.join(input_dir, fname)).convert("RGB")
        tensor = transform(img)
        torch.save(tensor, os.path.join(output_dir, fname.replace(".jpg", ".pt")))
