import matplotlib.pyplot as plt
from torchvision.utils import make_grid

def show_images(images, nrow=8):
    grid = make_grid(images, nrow=nrow, normalize=True)
    plt.figure(figsize=(12, 3))
    plt.imshow(grid.permute(1, 2, 0).cpu())
    plt.axis('off')
    plt.show()
