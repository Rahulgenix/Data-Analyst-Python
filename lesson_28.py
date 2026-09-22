import pandas as pd
sales = pd.Series([
    45000, 52000, 48000, 65000, 72000, 85000
])

def calculate_total(data):
    total = data.sum()
    return total

result = calculate_total(sales)
print("Total sales", result)

def calculate_kpis(data):
    total = data.sum()
    average = data.mean()
    highest = data.max()
    lowest = data.min()
    count = data.count()
    return total, average, highest, lowest, count

total, average, highest, lowest, count =calculate_kpis(sales)

print("\n---KIP SUMMARY---")
print("Total Sales:", total)
print("Average Sales:", round(average, 2))
print("Highest Sales:", highest)
print("Lowest Sales:", lowest)
print("Total Records:", count)


def sales_category(amount):
    if amount >=70000:
        return "high"
    elif amount >=50000:
        return "medim"
    else:
        return "low"

df = pd.DataFrame({
    "Employee": [
        "aman",
        "neha",
        "rahul",
        "priya",
        "sonali",
        "simran"
    ],
    "sales": sales
})

df["performance"] = df["sales"].apply(sales_category)

print("\nemployee performance")
print(df)