import pandas as pd

data = {
    "Customer": [
     "  rahul rajput ",
        "AMAN",
        " neha",
        "Priya ",
        "rahul rajput"
    ],
    "City": [
        "delhi",
        "NOIDA",
        "Delhi ",
        "noida",
        "delhi"
    ],
    "Sales": [
        "50000",
        "40000",
        "not available",
        "35000",
        "50000"
    ]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("\nOriginal data Types:")
print(df.dtypes)

df["Customer"] = df["Customer"].str.strip()
df["City"] = df["City"].str.title()

 
df["Customer"] = df["Customer"].str.title()
df["City"] = df["City"].str.title()


df["Sales"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

average_sales = df["Sales"].mean()
df["Sales"] = df["Sales"].fillna(average_sales)

df = df.drop_duplicates()


print("\nCleaned Data:")
print(df)

print("\nCleaned Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())
