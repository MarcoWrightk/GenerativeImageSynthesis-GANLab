def test_unlearning_effectiveness():
    model = torch.load("models/age_predictor.pt")
    forget_ids = [0, 1, 2]
    retain, forget = split_forget_retain(dataset, forget_ids)
    retrained = retrain_model(model, retain)
    assert not any(id in retrained.memory for id in forget_ids)
