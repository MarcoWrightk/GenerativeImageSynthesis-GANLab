import os
from PIL import Image

def preprocess_landscapes(input_dir, output_dir, size=(128, 128)):
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        try:
            img = Image.open(os.path.join(input_dir, fname)).convert("RGB")
            img = img.resize(size)
            img.save(os.path.join(output_dir, fname))
        except Exception as e:
            print(f"Error with {fname}: {e}")

