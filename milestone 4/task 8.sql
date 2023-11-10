SELECT
    SUM(o.order_amount) AS total_sales,
    s.store_type,
    s.country_code
FROM
    orders_table o
JOIN
    dim_store_details s ON o.store_code = s.store_code
WHERE
    s.country_code = 'DE'
GROUP BY
    s.store_type, s.country_code
ORDER BY
    total_sales DESC;
