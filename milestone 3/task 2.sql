ALTER TABLE dim_user_table
ALTER COLUMN first_name     TYPE VARCHAR(255),
ALTER COLUMN last_name      TYPE VARCHAR(255),
ALTER COLUMN date_of_birth  TYPE DATE,
ALTER COLUMN country_code   TYPE VARCHAR(3),
ALTER COLUMN user_uuid      TYPE UUID,
ALTER COLUMN join_date      TYPE DATE;
