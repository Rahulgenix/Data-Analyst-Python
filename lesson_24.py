import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104],
    "Customer_Name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
})

orders = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer_ID": [101, 103, 101, 105],
    "Product": ["Laptop", "Mobile", "Headphones", "Tablet"],
    "Amount": [55000, 25000, 5000, 30000]
})

# print("Customers Table:")
# print(customers)
# print("\nOrders Table:")
# print(orders)

inner_join = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
)

print("\nInner Join Result:")
print(inner_join)



left_join = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="left"
)       

print("\nLeft Join Result:")
print(left_join)



inner_result = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
)

print("\nInner Join:")
print(inner_result)


customer_sales = (
    inner_result.groupby(
        ["Customer_ID", "Customer_Name"],
        as_index=False
    )["Amount"].sum()
)

customer_sales = customer_sales.sort_values(
    by="Amount",
    ascending=False
)

print("\nCustomer-wise Sales:")
print(customer_sales)