import os
import gdown

def download_lsun(output_dir="interiors/raw"):
    os.makedirs(output_dir, exist_ok=True)
    url = "https://drive.google.com/uc?id=wright_LSUN_ID" 
    output_path = os.path.join(output_dir, "lsun_bedrooms.zip")
    gdown.download(url, output_path, quiet=False)
    print(f"Dowloaded in: {output_path}")

