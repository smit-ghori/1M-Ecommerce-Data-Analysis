import os
from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

root = Path(__file__).resolve().parent
os.chdir(root)

df = pd.read_csv("ecommerce_data_1M.csv")

df["age_group"] = pd.cut(
    df["age"],
    bins=[18, 25, 35, 45, 60, 80],
    labels=["18-25", "26-35", "36-45", "46-60", "60+"],
)
df["order_date"] = pd.to_datetime(df["order_date"])
df["order_month"] = df["order_date"].dt.to_period("M")

img_dir = root / "images"
img_dir.mkdir(exist_ok=True)

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="gender")
plt.title("Gender Distribution of Customers")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(img_dir / "gender_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 5))
top_city = df["city"].value_counts().head(10)
top_city.plot(kind="bar")
plt.title("Top 10 Cities by Number of Orders")
plt.xlabel("City")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(img_dir / "top_cities_orders.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8, 5))
result = (
    df.groupby("age_group")["total_amount"].sum().sort_values(ascending=False) / 1e7
)
bars = plt.bar(result.index.astype(str), result.values)
plt.title("Total Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Sales (₹ Crores)")
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
    )
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(img_dir / "sales_by_age_group.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 5))
category_revenue = (
    df.groupby("product_category")["total_amount"].sum().sort_values(ascending=False)
)
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig(img_dir / "revenue_by_category.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(12, 5))
monthly_revenue = df.groupby("order_month")["total_amount"].sum()
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig(img_dir / "monthly_revenue.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 5))
return_result = df.groupby("product_category").agg(
    Total_orders=("is_returned", "count"), Returned=("is_returned", "sum")
)
return_result["Returned_rate"] = (
    return_result["Returned"] / return_result["Total_orders"] * 100
).round(2)
return_result["Returned_rate"].sort_values(ascending=False).plot(kind="bar")
plt.title("Return Rate by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Return Rate (%)")
plt.tight_layout()
plt.savefig(img_dir / "return_rate_by_category.png", dpi=300, bbox_inches="tight")
plt.close()

print("Generated files:")
for f in sorted(img_dir.glob("*.png")):
    print(f.name, f.stat().st_size)
