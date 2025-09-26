# landscape_dataset.py
from torchvision import transforms
from torch.utils.data import Dataset
from PIL import Image
import os

class LandscapeDataset(Dataset):
    def __init__(self, folder):
        self.files = [os.path.join(folder, f) for f in os.listdir(folder)]
        self.transform = transforms.Compose([
            transforms.Resize(128),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5])
        ])

    def __getitem__(self, index):
        img = Image.open(self.files[index]).convert("RGB")
        return self.transform(img)

    def __len__(self):
        return len(self.files)
