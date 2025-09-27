import os
import gdown

def download_places365(output_dir="landscapes/raw"):
    os.makedirs(output_dir, exist_ok=True)
    url = "https://drive.google.com/uc?id=my_PLACES365_ID" 
    output_path = os.path.join(output_dir, "places365.zip")
    gdown.download(url, output_path, quiet=False)
    print(f"Dowloaded in: {output_path}")

