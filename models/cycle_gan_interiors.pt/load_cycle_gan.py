import torch

def load_cycle_gan(path="models/cycle_gan_interiors.pt"):
    model = torch.load(path)
    model.eval()
    return model
