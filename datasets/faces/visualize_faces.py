# visualize_faces.py
import matplotlib.pyplot as plt
from torchvision.utils import make_grid

def show_batch(images):
    grid = make_grid(images, nrow=8, normalize=True)
    plt.figure(figsize=(12, 2))
    plt.imshow(grid.permute(1, 2, 0).cpu())
    plt.axis('off')
    plt.show()
