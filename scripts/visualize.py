import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from logger import logger
from config import DATABASE_PATH, VISUALIZATION_PATH

Path(VISUALIZATION_PATH).mkdir(exist_ok=True)

sns.set_style("whitegrid")


# Chart 1: Monthly Sales Trend
def plot_monthly_sales(conn):
    query = """
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(12,6))

    sns.lineplot(data=df, x="month", y="total_sales", marker="o")

    plt.xticks(rotation=45)

    plt.title("Monthly Sales")

    plt.tight_layout()

    plt.savefig(
    Path(VISUALIZATION_PATH) / "monthly_sales.png"
    )

    plt.close()

    logger.info("Monthly sales chart generated.")


# Chart 2: Sales by Category
def plot_sales_by_category(conn):
    query = """
    SELECT
    category,
    SUM(sales) total_sales
    FROM sales
    GROUP BY category
    ORDER BY total_sales DESC
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(8,5))

    sns.barplot(data=df,x="category",y="total_sales")

    plt.title("Sales by Category")

    plt.tight_layout()

    plt.savefig(
        Path(VISUALIZATION_PATH) / "sales_by_category.png"
    )

    plt.close()

    logger.info("Sales by category chart generated.")


# Chart 3: Profit by Region
def plot_profit_by_region(conn):
    query = """
    SELECT
    region,
    SUM(profit) total_profit
    FROM sales
    GROUP BY region
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(8,5))

    sns.barplot(data=df,x="region",y="total_profit")

    plt.title("Profit by Region")

    plt.tight_layout()

    plt.savefig(
        Path(VISUALIZATION_PATH) / "profit_by_region.png"
    )

    plt.close()

    logger.info("Profit by region chart generated.")


# Chart 4: Top 10 Customers
def plot_top_customers(conn):
    query = """
    SELECT
    customer_name,
    SUM(sales) total_sales
    FROM sales
    GROUP BY customer_name
    ORDER BY total_sales DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10,6))

    sns.barplot(data=df,y="customer_name",x="total_sales")

    plt.title("Top 10 Customers")

    plt.tight_layout()

    plt.savefig(
        Path(VISUALIZATION_PATH) / "top_customers.png"
    )

    plt.close()

    logger.info("Top customers chart generated.")



# Chart 5: Discount vs Profit 
# Discount vs Profit (Scatter Plot)
def plot_discount_vs_profit(conn):
    query = """
    SELECT
        discount,
        profit,
        category
    FROM sales;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="discount",
        y="profit",
        hue="category",
        alpha=0.7
    )

    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit")

    plt.tight_layout()

    plt.savefig(
        Path(VISUALIZATION_PATH) / "discount_vs_profit.png"
    )

    plt.close()

    logger.info("Discount vs profit chart generated.")


# Chart 6: Sales Distribution
# Sales Distribution (Histogram)
def plot_sales_distribution(conn):
    query = """
    SELECT
        sales
    FROM sales;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(8, 6))

    sns.histplot(
        data=df,
        x="sales",
        bins=30,
        kde=True
    )

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        Path(VISUALIZATION_PATH) / "sales_distribution.png"
    )

    plt.close()

    logger.info("Sales distribution chart generated.")


def generate_visualizations():
    """
    Generate all project visualizations.
    """

    conn = sqlite3.connect(DATABASE_PATH)

    plot_monthly_sales(conn)
    plot_sales_by_category(conn)
    plot_profit_by_region(conn)
    plot_top_customers(conn)
    plot_discount_vs_profit(conn)
    plot_sales_distribution(conn)

    conn.close()

    logger.info("All visualizations generated successfully.")

    print("✅ All visualizations generated successfully.")