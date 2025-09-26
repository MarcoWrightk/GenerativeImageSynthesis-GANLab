# preprocess_faces.py
from PIL import Image
import os

def preprocess_faces(input_dir, output_dir, size=(64, 64)):
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        img = Image.open(os.path.join(input_dir, fname)).convert("RGB")
        img = img.resize(size)
        img.save(os.path.join(output_dir, fname))
