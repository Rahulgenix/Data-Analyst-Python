import pandas as pd

data = {
    "Order_Date": [
        "2026-01-10",
        "2026-01-20",
        "2026-02-05",
        "2026-02-18",
        "2026-03-12",
        "2026-03-25"
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Chair",
        "Laptop",
        "Mobile",
        "Table"
    ],
    "Sales": [55000, 25000, 8000, 60000, 30000, 12000]
}

df = pd.DataFrame(data)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print(df)
print("\nData Types:")
print(df.dtypes)


df["Year"] = df["Order_Date"].dt.year
df["Month_Number"] = df["Order_Date"].dt.month
df["Month"] = df["Order_Date"].dt.month_name()
df["Day"] = df["Order_Date"].dt.day
df["Day_Name"] = df["Order_Date"].dt.day_name()

print("\nData with Date Columns:")
print(df)



monthly_sales = df.groupby(
    ["Month_Number", "Month"]
)["Sales"].sum().reset_index()

monthly_sales = monthly_sales.sort_values("Month_Number")

print("\nMonthly Sales:")
print(monthly_sales[["Month", "Sales"]])


february_data = df[df["Month"] == "February"]

print("\nFebruary Orders:")
print(february_data)