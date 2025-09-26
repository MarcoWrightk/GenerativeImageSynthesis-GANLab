# visualize_landscapes.py
def show_landscape_sample(dataset, index=0):
    import matplotlib.pyplot as plt
    img = dataset[index]
    plt.imshow(img.permute(1, 2, 0).cpu())
    plt.axis('off')
    plt.show()
