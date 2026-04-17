def analyze_scores(scores):
    avg = sum(scores) / len(scores)
    return avg, max(scores), min(scores)

average, highest, lowest = analyze_scores([70, 80, 90])

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)