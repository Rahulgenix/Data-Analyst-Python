import numpy as np
sales = np.array([45000, 52000, 48000, 65000, 72000, 85000])

print("Sales Data:", sales)
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))
print("median Sales:", np.median(sales))
print("Standard Deviation of Sales:", np.std(sales))

tax = sales * 0.18
final_sales = sales + tax

print("\nTax:")
print(tax)

print("\nSales After Tax:")
print(final_sales)


categories = np.where(
    sales >= 60000,
    "High",
    "Low"
)

print("\nSales Categories:")
print(categories)