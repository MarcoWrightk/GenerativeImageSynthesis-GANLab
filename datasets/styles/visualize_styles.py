# visualize_styles.py
def show_style_examples(folder, n=5):
    import matplotlib.pyplot as plt
    from PIL import Image
    import os
    files = os.listdir(folder)[:n]
    fig, axes = plt.subplots(1, n, figsize=(15, 3))
    for i, f in enumerate(files):
        img = Image.open(os.path.join(folder, f))
        axes[i].imshow(img)
        axes[i].axis('off')
    plt.show()
