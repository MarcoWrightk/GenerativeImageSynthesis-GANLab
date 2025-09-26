import torch

def load_conditional_gan(path="models/conditional_gan_posters.pt"):
    model = torch.load(path)
    model.eval()
    return model
