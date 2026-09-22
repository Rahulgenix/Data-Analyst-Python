import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order_Date": [
        "2026-01-10", "2026-01-18",
        "2026-02-05", "2026-02-20",
        "2026-03-08", "2026-03-25",
        "2026-04-12", "2026-04-28"
    ],
    "Product": [
        "Laptop", "Mobile", "Chair", "Laptop",
        "Mobile", "Table", "Laptop", "Chair"
    ],
    "Category": [
        "Electronics", "Electronics", "Furniture", "Electronics",
        "Electronics", "Furniture", "Electronics", "Furniture"
    ],
    "Region": [
        "North", "South", "North", "West",
        "South", "East", "North", "West"
    ],
    "Quantity": [1, 2, 3, 1, 2, 2, 1, 4],
    "Price": [55000, 25000, 5000, 60000, 28000, 8000, 58000, 4500]
}

df = pd.DataFrame(data)

# Data preparation
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month_Number"] = df["Order_Date"].dt.month
df["Month"] = df["Order_Date"].dt.month_name()



# print("First 5 Rows:"), 
# print(df.head())

# print("\nDataset Shape:", df.shape)

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nNumerical Summary:")
# print(df[["Quantity", "Price", "Revenue"]].describe())


total_revenue = df["Revenue"].sum()
average_order = df["Revenue"].mean()
total_orders = df["Order_Date"].count()
top_order = df["Revenue"].max()


print("\n---kpi summary---")
print("total_revenue", total_revenue)
print("Average Order Value:", round(average_order, 2))
print("Total Orders:", total_orders)
print("Highest Order Value:", top_order)


Product_sales = (
    df.groupby("Product") ["Revenue"].sum().sort_values(ascending=False)
)
category_sales = (
    df.groupby("Category") ["Revenue"].sum().sort_values(ascending=False)
)


region_sales = (
    df.groupby("Region") ["Revenue"].sum().sort_values(ascending=False)
)

region_sales = (
    df.groupby("Region") ["Revenue"].sum().sort_values(ascending=False)
)


print("\nProduct-wise Revenue:")
print(Product_sales)

print("\nCategory-wise Revenue:")
print(category_sales)

print("\nRegion-wise Revenue:")
print(region_sales)


monthly_sales = (
    df.groupby(["Month_Number", "Month"])["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Month_Number")
)


plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o",
    color="royalblue",
    linewidth=2
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("lesson_20_monthly_revenue.png", dpi=300)
plt.show()