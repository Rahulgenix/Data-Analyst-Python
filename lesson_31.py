import pandas as pd

data = {
    "Product": [
        "Laptop", "Mobile", "Chair", "Table",
        "Laptop", "Mobile", "Chair", "Headphones"
    ],
    "Category": [
        "Electronics", "Electronics", "Furniture", "Furniture",
        "Electronics", "Electronics", "Furniture", "Electronics"
    ],
    "Region": [
        "North", "South", "North", "East",
        "West", "South", "West", "North"
    ],
    "Quantity": [1, 2, 4, 2, 1, 3, 5, 4],
    "Price": [60000, 25000, 5000, 8000, 58000, 28000, 4500, 2000],
    "Cost": [48000, 20000, 3000, 5000, 46000, 22000, 2800, 1200]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Quantity"] * df["Price"]
# print(df)
print("Total Revenue:", df["Revenue"].sum())

df["Total_Cost"] = df["Quantity"] * df["Cost"]
print("total_cosr:", df["Total_Cost"].sum())

df["Profit"] = df["Revenue"] - df["Total_Cost"]
print("Total Profit:", df["Profit"].sum())


category_revenue = df.groupby("Category")["Revenue"].sum()
print("\nCategory-wise Revenue:")
print(category_revenue)


top_product = df.loc[df["Revenue"].idxmax()]
print("\nTop Product")
print(top_product[["Product", "Revenue"]])

high_revenue = df[df["Revenue"]>=50000]
print("\nHigh Revenue Records:")
print(high_revenue[["Product", "Revenue"]])