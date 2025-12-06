

def classify_day(transactions):
    total = sum(transactions)

    if total < 200:
        return "Loss"
    elif total < 500:
        return "Low Margin"
    elif total < 800:
        return "Healthy"
    else:
        return "Peak"

transactions = [500, 80, 89, 80, 90]


result = classify_day(transactions)
print("Day Classification:", result)
