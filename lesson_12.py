import pandas as pd

df = pd.read_csv("sales_data.csv")

print("complete data:")
print(df)

# print ("\nFirst 3 rows: ")
# print(df.head(3))  # Display the first 3 rows of the DataFrame

# print("\ndataset size:")
# print(df.shape)  # Display the number of rows and columns in the DataFrame

# print("\nColumn names:")
# print(df.columns)  # Display the column names of the DataFrame

# print("\ndataset information:")
# df.info()  # Display information about the DataFrame, including data types and non-null counts


df["Total_Amount"] = df["Quantity"] * df["Price"]

print("\nData with Total Amount:")
print(df)

print("\nGrand Total:", df["Total_Amount"].sum())