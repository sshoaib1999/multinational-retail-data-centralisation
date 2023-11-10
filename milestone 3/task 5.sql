-- Rename still_available to still_available_old
ALTER TABLE dim_products
RENAME COLUMN still_available TO still_available_old;

-- Change data types
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT,
ALTER COLUMN weight TYPE FLOAT,
ALTER COLUMN EAN TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN product_code TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID,
ALTER COLUMN still_available_old TYPE BOOL,
ALTER COLUMN weight_class TYPE VARCHAR(?); -- Replace ? with the actual maximum length

-- Drop still_available_old column
ALTER TABLE dim_products
DROP COLUMN still_available_old;
