import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Chair",
        "Table",
        "Headphones",
        "Keyboard"
    ],
    "Sales": [55000, 50000, 20000, 16000, 6000, 7500]
}

df = pd.DataFrame(data)

plt.bar(df["Product"], df["Sales"], color="royalblue")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()