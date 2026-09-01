def list_expenses(data):
    if not data:
        print("No records found.")
        return

    for i, d in enumerate(data, 1):
        print(f"{i}. {d['amount']:<8.2f}| {d['category']:<10}| {d['date']:<8}| {d['note']:<15}|")

def filter_by_category(data, category):
    filtered = [d for d in data if d['category'] == category]

    return filtered

def filter_by_month(data, month):
    filtered = [d for d in data if d['date'].startswith(month)]
    
    return filtered

def monthly_summary(data, month):
    filtered = filter_by_month(data, month)

    summary = {}
    for m in filtered:
        summary[m['category']] = summary.get(m['category'], 0) + m['amount']

    if not summary:
        print(f"No expenses for '{month}'")
        return

    total = 0
    for s in summary.values():
        total += s

    print(f"\nSummary for {month}:")
    for k, v in summary.items():
        print(f"{k:<10}: {v:>8.2f}")
    print("-"* 15)
    print(f"Total: {total:<8.2f}\n")

def get_filtered_list(data, category=None, month=None):
    filtered = data
    if category is not None:
        filtered = filter_by_category(filtered, category)
    if month is not None:
        filtered = filter_by_month(filtered, month)
    return filtered