ALTER TABLE orders_table
ALTER COLUMN date_uuid        TYPE UUID,
ALTER COLUMN user_uuid        TYPE UUID,
ALTER COLUMN card_number      TYPE VARCHAR(16),
ALTER COLUMN store_code       TYPE VARCHAR(10),
ALTER COLUMN product_code     TYPE VARCHAR(10),
ALTER COLUMN product_quantity TYPE SMALLINT;
