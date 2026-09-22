import sqlite3
import pandas as pd


connection = sqlite3.connect("sales_database.db")
print("Database connected successfully.")


data = {
    "Orderrr_id":[101, 102, 103, 104, 105, 106],
    "Customer":["aman", "neha", "rahul", "priya", 'roshni', "simran"],
    "Category": ["Electronics",
        "Furniture",
        "Electronics",
        "Furniture",
        "Electronics",
        "Electronics"],

"Region": ["North", "South", "North", "East", "West", "South"],
"Sales": [55000, 20000, 75000, 30000, 65000, 80000]
}

df = pd.DataFrame(data)
print("\nOriginal data:")
print(df)

df.to_sql(
    "sales", connection, 
    if_exists="replace", index=False

)
print("\ndata saved into sql tabal")

query = """
SELECT
    Customer, 
    Category, 
    Region, 
    Sales 
    FROM sales
WHERE Sales .= 50000
ORDER BY Sales DESC;
"""
result = pd.read_dl_query(query, connection)
print("\nSales 50000 or more:")
print(result)