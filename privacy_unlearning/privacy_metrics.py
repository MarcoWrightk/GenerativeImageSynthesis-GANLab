def measure_forgetting(original_model, retrained_model, forget_loader):
    original_preds = [original_model(x.unsqueeze(0)).argmax().item() for x, _ in forget_loader]
    retrained_preds = [retrained_model(x.unsqueeze(0)).argmax().item() for x, _ in forget_loader]
    mismatch = sum(o != r for o, r in zip(original_preds, retrained_preds))
    return mismatch / len(forget_loader)
