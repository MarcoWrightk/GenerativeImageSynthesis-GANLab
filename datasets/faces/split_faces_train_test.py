# split_faces_train_test.py
import os, shutil
from sklearn.model_selection import train_test_split

def split_dataset(input_dir, output_dir, test_size=0.2):
    files = os.listdir(input_dir)
    train, test = train_test_split(files, test_size=test_size)
    os.makedirs(f"{output_dir}/train", exist_ok=True)
    os.makedirs(f"{output_dir}/test", exist_ok=True)
    for f in train:
        shutil.copy(os.path.join(input_dir, f), f"{output_dir}/train/{f}")
    for f in test:
        shutil.copy(os.path.join(input_dir, f), f"{output_dir}/test/{f}")
