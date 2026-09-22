import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Product": [
        "Laptop", "Mobile", "Chair", "Laptop",
        "Mobile", "Table", "Laptop", "Chair"
    ],
    "Category": [
        "Electronics", "Electronics", "Furniture", "Electronics",
        "Electronics", "Furniture", "Electronics", "Furniture"
    ],
    "Region": [
        "North", "South", "North", "West",
        "South", "East", "North", "West"
    ],
    "Revenue": [55000, 25000, 5000, 60000, 28000, 8000, 58000, 4500]
}

df =pd.DataFrame(data)
sns.set_theme(style="whitegrid")

category_sales = (
    df.groupby("Category", as_index=False)["Revenue"].sum()
)

sns.barplot(
    data=category_sales,
    x="Category",
    y="Revenue",
    hue="Category",
    palette="Blues_d",
    legend=False
)


# plt.title("Category-wise Revenue")
# plt.xlabel("Category")
# plt.ylabel("Total Revenue")
# plt.tight_layout()
# # plt.savefig("category_revenue.png",  dpi=300)
# plt.show()

region_sales = (
    df.groupby("Region", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
)

sns.barplot(
    data=region_sales,
    x="Revenue",
    y="Region",
    hue="Region",
    palette="Blues_d",
    legend=False
)   

plt.title("Region-wise Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Region")
plt.tight_layout()
# plt.savefig("region_revenue.png",  dpi=300)
plt.show()