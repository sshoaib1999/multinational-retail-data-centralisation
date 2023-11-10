SELECT
    COUNT(*) AS numbers_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN location = 'Web' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM
    orders_table
GROUP BY
    location;
