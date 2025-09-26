import torch

def load_age_predictor(path="models/age_predictor_unlearned.pt"):
    model = torch.load(path)
    model.eval()
    return model
