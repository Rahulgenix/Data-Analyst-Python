import pandas as pd 
data = {

"product": ["Laptop", "Mobile", "Tablet", "Desktop", "Mobile"],
"category": ["Electronics",
        "Electronics",
        "Furniture",
        "Furniture",
        "Electronics",
       ],
"quantity": [1,2,4,2,3],
"price": [50000, 20000, 15000, 30000, 25000]

}
df = pd.DataFrame(data)
df["total_amount"] = df["quantity"] * df["price"]
print("complete data:")
print(df)



average_sales =df.groupby("category")["total_amount"].mean()
print("\ncategory-wise average sales:")
print(average_sales)



# summary = df.groupby("Category")["Total_Amount"].agg(
#     ["sum", "mean", "max", "min", "count"]
# )

# print("\nCategory Summary:")
# print(summary)