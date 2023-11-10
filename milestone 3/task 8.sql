-- Add primary key constraint to dim_user_table
ALTER TABLE dim_user_table
ADD PRIMARY KEY (user_uuid);

-- Add foreign key constraint in orders_table
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_user
FOREIGN KEY (user_uuid)
REFERENCES dim_user_table(user_uuid);

-- Repeat the process for other dim tables and orders_table columns
