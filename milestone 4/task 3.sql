SELECT
    SUM(order_amount) AS total_sales,
    EXTRACT(MONTH FROM date_added) AS month
FROM
    orders_table o
JOIN
    dim_date_times d ON o.date_uuid = d.date_uuid
GROUP BY
    month
ORDER BY
    total_sales DESC, month
LIMIT 6;
