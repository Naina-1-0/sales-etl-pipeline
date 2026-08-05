-- Total Sales
SELECT ROUND(SUM(sales), 2) AS total_sales, 
FROM sales;

-- Total Profit
SELECT ROUND(SUM(profit), 2) AS total_profit, 
FROM sales;

-- Top 10 Customers by Total Sales
SELECT 
    customer_name, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by Region
SELECT 
    region, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

--Profit by Product Category
SELECT
    category,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC;

-- Top 10 Products
SELECT 
    product_name, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Monthly Sales
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;

-- Top 5 States by Profit
SELECT state, ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY state
ORDER BY total_profit DESC
LIMIT 5;

-- Orders by Profitability
SELECT
    order_id, sales, profit,
    CASE
        WHEN profit > 100 THEN 'High Profit'
        WHEN profit > 0 THEN 'Profit'
        ELSE 'Loss'
    END AS order_status
FROM sales;

-- Discount Categories
SELECT
    product_name, discount,
    CASE
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount <= 0.20 THEN 'Low Discount'
        ELSE 'High Discount'
    END AS discount_level
FROM sales;

-- Ranking Customers by Sales
SELECT
    customer_name, ROUND(SUM(sales),2) AS total_sales, RANK() 
    OVER(
        ORDER BY SUM(sales) DESC
    ) AS sales_rank
FROM sales
GROUP BY customer_name;

-- Dense Ranking States by Profit
SELECT
    state, ROUND(SUM(profit),2) AS profit,
    DENSE_RANK() OVER(
        ORDER BY SUM(profit) DESC
    ) AS rank_profit
FROM sales
GROUP BY state;


-- Top 5 Customers
WITH customer_sales AS (
SELECT
    customer_name,
    SUM(sales) total_sales
FROM sales
GROUP BY customer_name
)

SELECT *
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 5;


-- Profitable States
WITH state_profit AS (
SELECT
    state,
    SUM(profit) total_profit
FROM sales
GROUP BY state
)
SELECT *
FROM state_profit
WHERE total_profit > 10000;

-- Monthly Sales Trend
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY month
ORDER BY month;

-- Highest Profit Margin Products
SELECT
    product_name,
    ROUND(AVG(profit_margin),2) AS avg_margin
FROM sales
GROUP BY product_name
ORDER BY avg_margin DESC
LIMIT 10;

-- Loss Making Products
SELECT
    product_name,
    ROUND(SUM(profit),2) AS total_loss
FROM sales
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_loss;

-- Top Product in Each Category
WITH ranked_products AS (
    SELECT
        category, product_name, SUM(sales) total_sales,
        ROW_NUMBER() OVER(
            PARTITION BY category
            ORDER BY SUM(sales) DESC
        ) rn
    FROM sales
    GROUP BY category, product_name
)

SELECT *
FROM ranked_products
WHERE rn = 1;

