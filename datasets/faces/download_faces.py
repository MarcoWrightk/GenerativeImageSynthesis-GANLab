import os
import gdown

def download_celeba(output_dir="faces/raw"):
    os.makedirs(output_dir, exist_ok=True)
    url = "https://drive.google.com/uc?id=1u1zvZkVZrZKZKZKZKZKZKZKZKZKZKZKZ"  # Reemplaza con el ID real
    output_path = os.path.join(output_dir, "celeba.zip")
    gdown.download(url, output_path, quiet=False)
    print(f"Descargado en: {output_path}")

