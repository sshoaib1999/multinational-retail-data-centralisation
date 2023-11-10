WITH MonthlySales AS (
    SELECT
        EXTRACT(YEAR FROM d.date_added) AS year,
        EXTRACT(MONTH FROM d.date_added) AS month,
        SUM(o.order_amount) AS total_sales
    FROM
        orders_table o
    JOIN
        dim_date_times d ON o.date_uuid = d.date_uuid
    GROUP BY
        year, month
)
SELECT
    total_sales,
    year,
    month
FROM
    MonthlySales
ORDER BY
    total_sales DESC
LIMIT 10;
