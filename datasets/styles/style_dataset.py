import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

class StyleDataset(Dataset):
    def __init__(self, folder, image_size=256):
        self.files = [os.path.join(folder, f) for f in os.listdir(folder)]
        self.transform = transforms.Compose([
            transforms.Resize((image_size, image_size)),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5])
        ])

    def __getitem__(self, index):
        img = Image.open(self.files[index]).convert("RGB")
        return self.transform(img)

    def __len__(self):
        return len(self.files)

