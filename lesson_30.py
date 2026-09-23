import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv("sales_project.csv")

# Data cleaning
df.columns = df.columns.str.strip()
df["Customer"] = df["Customer"].str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df = df.drop_duplicates()

# Calculated columns
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df["Total_Cost"] = df["Quantity"] * df["Unit_Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]

df["Month_Number"] = df["Order_Date"].dt.month
df["Month"] = df["Order_Date"].dt.month_name()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv("sales_project.csv")

# Data cleaning
df.columns = df.columns.str.strip()
df["Customer"] = df["Customer"].str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df = df.drop_duplicates()

# Calculated columns
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df["Total_Cost"] = df["Quantity"] * df["Unit_Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]

df["Month_Number"] = df["Order_Date"].dt.month
df["Month"] = df["Order_Date"].dt.month_name()


total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("\n--- SALES KPI REPORT ---")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")


category_summary = (
    df.groupby("Category", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Revenue", ascending=False)
)

region_summary = (
    df.groupby("Region", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

monthly_summary = (
    df.groupby(["Month_Number", "Month"], as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Month_Number")
)

print("\nCategory Summary:")
print(category_summary)

print("\nRegion Summary:")
print(region_summary)

print("\nMonthly Summary:")
print(monthly_summary)


sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

sns.barplot(
    data=category_summary,
    x="Category",
    y="Revenue",
    hue="Category",
    legend=False,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Category-wise Revenue")

sns.barplot(
    data=region_summary,
    x="Region",
    y="Revenue",
    hue="Region",
    legend=False,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Region-wise Revenue")

axes[1, 0].plot(
    monthly_summary["Month"],
    monthly_summary["Revenue"],
    marker="o",
    linewidth=2,
    color="royalblue"
)
axes[1, 0].set_title("Monthly Revenue Trend")
axes[1, 0].tick_params(axis="x", rotation=30)

sns.barplot(
    data=category_summary,
    x="Category",
    y="Profit",
    hue="Category",
    legend=False,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Category-wise Profit")

plt.suptitle(
    "E-commerce Sales Analysis Dashboard",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=300)
plt.show()



kpi_report = pd.DataFrame({
    "KPI": [
        "Total Revenue",
        "Total Profit",
        "Total Orders",
        "Average Order Value",
        "Profit Margin (%)"
    ],
    "Value": [
        total_revenue,
        total_profit,
        total_orders,
        round(average_order_value, 2),
        round(profit_margin, 2)
    ]
})

with pd.ExcelWriter(
    "sales_analysis_report.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )

    kpi_report.to_excel(
        writer,
        sheet_name="KPI Report",
        index=False
    )

    category_summary.to_excel(
        writer,
        sheet_name="Category Analysis",
        index=False
    )

    region_summary.to_excel(
        writer,
        sheet_name="Region Analysis",
        index=False
    )

    monthly_summary.to_excel(
        writer,
        sheet_name="Monthly Analysis",
        index=False
    )

print("\nProject completed successfully.")