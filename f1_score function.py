def f1_score(tp, fp, fn):
    # Check if tp, fp, fn are integers
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        print("tp, fp, and fn must be integers")
        return None

    # Check if tp, fp, fn are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return None
    
    # Calculate precision, recall and F1 Score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score_cal = 2 * (precision * recall) / (precision + recall)
    
    # Print precision, recall and F1 score
    print(f"precison is {precision}")
    print(f"recall is {recall}")
    print(f"F1-Score is {f1_score_cal}")