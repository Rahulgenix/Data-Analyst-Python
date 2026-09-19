import pandas as pd

data = {

"product":["Laptop",
        "Mobile",
        "Chair",
        "Table",
        "Headphones",
        "Keyboard"],
"category": [
    "Electronics",
        "Electronics",
        "Furniture",
        "Furniture",
        "Electronics",
        "Electronics"
        ],

"Quantity": [1, 2, 4, 2, 3, 5],
"Price": [55000, 25000, 5000, 8000, 2000, 1500]

}
df = pd.DataFrame(data)
df["total_amount"] = df["Quantity"] * df["Price"]

print("complete data:")
print(df)

#sort data ascending=False ascending=True

sorted_data = df.sort_values(
    by="total_amount",
    ascending=False
)
print("\nhighest to lowest sales:")
print(sorted_data)

# low salesing product

lowest_product = df.nsmallest(1, "total_amount")
print("\nlowest selling product:")
print(lowest_product[["product", "category", "total_amount"]])


#noumber of products

category_count = df["category"].value_counts()
print(category_count)