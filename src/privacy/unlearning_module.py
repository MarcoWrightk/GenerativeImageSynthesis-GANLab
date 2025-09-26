import torch

def unlearn_predictor(model, forget_loader, retain_loader, epochs=10):
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    criterion = torch.nn.CrossEntropyLoss()

    # Retrain only on retain set
    for epoch in range(epochs):
        for x, y in retain_loader:
            preds = model(x)
            loss = criterion(preds, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    return model

