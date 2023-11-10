WITH SaleTime AS (
    SELECT
        EXTRACT(YEAR FROM d.date_added) AS year,
        LEAD(d.date_added) OVER (PARTITION BY EXTRACT(YEAR FROM d.date_added) ORDER BY d.date_added) AS next_sale_date,
        d.date_added
    FROM
        orders_table o
    JOIN
        dim_date_times d ON o.date_uuid = d.date_uuid
)
SELECT
    year,
    AVG(next_sale_date - date_added) AS actual_time_taken
FROM
    SaleTime
GROUP BY
    year
ORDER BY
    year;
