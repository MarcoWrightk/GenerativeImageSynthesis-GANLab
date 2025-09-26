# visualize_interiors.py
def show_interior_grid(dataset, n=6):
    import matplotlib.pyplot as plt
    from torchvision.utils import make_grid
    imgs = [dataset[i] for i in range(n)]
    grid = make_grid(imgs, nrow=n, normalize=True)
    plt.imshow(grid.permute(1, 2, 0).cpu())
    plt.axis('off')
    plt.show()
