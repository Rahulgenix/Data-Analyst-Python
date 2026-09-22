import pandas as pd

data = {
    "Region": [
        "North", "North", "South", "South",
        "East", "East", "West", "West"
    ],
    "Category": [
        "Electronics", "Furniture",
        "Electronics", "Furniture",
        "Electronics", "Furniture",
        "Electronics", "Furniture"
    ],
    "Sales": [
        85000, 30000,
        70000, 25000,
        60000, 35000,
        90000, 20000
    ],
    "Quantity": [3, 5, 2, 4, 2, 6, 4, 3]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

sales_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nSales Pivot Table:")
print(sales_pivot)