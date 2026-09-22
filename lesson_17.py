import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["January", "February", "March", "April", "May", "June"],
    "sales": [1500, 2000, 1800, 2200, 2500, 3000]
}

df = pd.DataFrame(data)
plt.plot(
    df["month"], df["sales"], marker="o", color="green", linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig("monthly_sales_trend.png", dpi=300)  # Save the plot as a PNG file
plt.show()  # Display the plot
# df["Growth"] = df["Growth"].round(2)
# df["Growth"] = df["Sales"].pct_change() * 100

# print(df)