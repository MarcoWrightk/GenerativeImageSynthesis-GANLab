import os
import gdown

def download_wikiart(output_dir="styles/raw"):
    os.makedirs(output_dir, exist_ok=True)
    url = "https://drive.google.com/uc?id=my_WIKIART_ID"  
    output_path = os.path.join(output_dir, "wikiart_styles.zip")
    gdown.download(url, output_path, quiet=False)
    print(f"Dowloaded in: {output_path}")

