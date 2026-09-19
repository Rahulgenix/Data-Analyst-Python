import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "department": ["HR", "IT", "Finance", "IT", "HR"],
    "salary": [50000, 60000, 55000, 70000, 55000]
}
df = pd.DataFrame(data)

# print("complete data")
# print(df)   

# print("\nOnly names: ")
# print(df["name"])  # Accessing a single column  

# print("\ntotal salary: ", df['salary'].sum())
# print("average salary: ", df['salary'].mean())
# print("highest salary: ", df["salary"].max())
# print("lowest salary: ", df["salary"].min())
# # print("total employees: ", df["name"].count())


# high_sales = df[df["Sales"] >= 50000]

# print("\nEmployees with Sales 50000 or more:")
# print(high_sales)


# sales_department = df[df["Department"] == "Sales"]

# print("\nSales Department:")
# print(sales_department)


# result = df[
#     (df["Department"] == "Sales") &
#     (df["Sales"] >= 90000)
# ]

# print("\nSales Department with Sales 90000 or more:")
# print(result)