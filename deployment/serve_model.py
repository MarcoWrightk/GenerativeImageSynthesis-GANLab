from flask import Flask, request, jsonify
import torch

app = Flask(__name__)
model = torch.load("models/dcgan_faces.pt")
model.eval()

@app.route("/generate", methods=["POST"])
def generate():
    z = torch.randn(1, 100, 1, 1)
    with torch.no_grad():
        img = model(z)
    return jsonify(img.tolist())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
