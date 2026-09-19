import pandas as pd
data = {
    "customer": ["Aman", "Neha", "Rahul", "Priya", "Rahul"],
    "City": ["Delhi", None, "Noida", "Delhi", "Noida"],
    "Sales": [50000, 40000, None, 30000, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


print("\nMissing values:")
print(df.isnull().sum())
df["City"] = df["City"].fillna("Unknown")

average_sales = df["Sales"].mean()
df["Sales"] = df["Sales"].fillna(average_sales)