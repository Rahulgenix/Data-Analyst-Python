import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = {
    "Advertising": [5000, 8000, 12000, 15000, 18000, 22000],
    "Visitors": [500, 750, 1100, 1350, 1600, 2000],
    "Orders": [25, 40, 58, 72, 85, 110],
    "Revenue": [50000, 75000, 110000, 140000, 165000, 210000],
    "Returns": [5, 6, 4, 8, 7, 9]
}
df = pd.DataFrame(data)

correlation = df.corr()
print("correlation matrix:")
print(correlation.round(2))  


plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()

revenue_correlation = (
    correlation["Revenue"].sort_values(ascending=False)
)
print("\nCorrelation with Revenue:")
print(revenue_correlation.round(2))