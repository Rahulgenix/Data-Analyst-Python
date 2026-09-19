import pandas as pd

data = {
    'name': ["aman", "rahul", "rohan", "priya"],
    'department': ["IT", "HR", "Finance", "Marketing"],
    'salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
#print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)