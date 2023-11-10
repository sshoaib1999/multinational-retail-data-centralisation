-- Add foreign key constraint to orders_table referencing dim_user_table
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_user
FOREIGN KEY (user_uuid)
REFERENCES dim_user_table(user_uuid);

-- Add foreign key constraints for other dim tables
-- Replace the column names and constraint names as needed
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_product
FOREIGN KEY (product_code)
REFERENCES dim_products(product_code);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_store
FOREIGN KEY (store_code)
REFERENCES dim_store_details(store_code);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_date
FOREIGN KEY (date_uuid)
REFERENCES dim_date_times(date_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_card
FOREIGN KEY (card_number)
REFERENCES dim_card_details(card_number);
