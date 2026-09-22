import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Employee": [
        "Aman", "Neha", "Rahul", "Priya", "Rohit",
        "Simran", "Karan", "Anjali", "Vikas", "Arjun"
    ],
    "Salary": [
        30000, 32000, 35000, 36000, 38000,
        40000, 42000, 45000, 48000, 500000
    ]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

sns.boxenplot(x=df["Salary"], color="skyblue")

plt.title("salary before oulier removal")
plt.tight_layout()
plt.show()

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 -Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR", IQR)
print("lower limit:", lower_limit)
print("Upper limit:",upper_limit)
outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print("\nDetected Outliers:")
print(outliers)

cleaned_df = df[
    (df["Salary"] >= lower_limit) &
    (df["Salary"] <= upper_limit)
]

print("\nData After Outlier Removal:")
print(cleaned_df)

sns.boxplot(x=cleaned_df["Salary"], color="lightgreen")

plt.title("Salary After Outlier Removal")
plt.tight_layout()
plt.show()

sns.boxplot(x=cleaned_df["Salary"], color="lightgreen")

plt.title("Salary After Outlier Removal")
plt.tight_layout()
plt.show()