
import torch
import torch.nn as nn
from torchvision import models

class VGGFeatures(nn.Module):
    def __init__(self):
        super().__init__()
        self.vgg = models.vgg19(pretrained=True).features[:21].eval()

    def forward(self, x):
        return self.vgg(x)

def compute_style_loss(style_features, generated_features):
    loss = 0
    for sf, gf in zip(style_features, generated_features):
        loss += torch.mean((gram_matrix(sf) - gram_matrix(gf))**2)
      return loss 

def gram_matrix(tensor):
    b, c, h, w = tensor.size()
    features = tensor.view(b, c, h * w)
    G = torch.bmm(features, features.transpose(1, 2))
    return G / (c * h * w)
