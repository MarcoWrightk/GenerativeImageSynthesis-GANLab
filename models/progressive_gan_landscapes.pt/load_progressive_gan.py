import torch

def load_progressive_gan(path="models/progressive_gan_landscapes.pt"):
    model = torch.load(path)
    model.eval()
    return model
