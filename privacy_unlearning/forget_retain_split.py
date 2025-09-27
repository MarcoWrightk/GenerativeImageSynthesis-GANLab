def split_forget_retain(dataset, forget_ids):
    retain = [x for i, x in enumerate(dataset) if i not in forget_ids]
    forget = [x for i, x in enumerate(dataset) if i in forget_ids]
    return retain, forget
