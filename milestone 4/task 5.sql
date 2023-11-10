SELECT
    store_type,
    SUM(order_amount) AS total_sales,
    (SUM(order_amount) / (SELECT SUM(order_amount) FROM orders_table)) * 100 AS percentage_total
FROM
    orders_table
GROUP BY
    store_type
ORDER BY
    total_sales DESC;
