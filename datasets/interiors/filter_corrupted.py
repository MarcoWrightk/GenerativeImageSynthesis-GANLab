# filter_corrupted.py
from PIL import Image

def clean_dataset(folder):
    for fname in os.listdir(folder):
        try:
            Image.open(os.path.join(folder, fname)).verify()
        except:
            os.remove(os.path.join(folder, fname))
