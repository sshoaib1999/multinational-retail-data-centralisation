-- Merge latitude_2 into latitude
UPDATE store_details_table
SET latitude = COALESCE(latitude, latitude_2);

-- Drop the latitude_2 column
ALTER TABLE store_details_table
DROP COLUMN latitude_2;

-- Change data types
ALTER TABLE store_details_table
ALTER COLUMN longitude     TYPE FLOAT,
ALTER COLUMN locality      TYPE VARCHAR(255),
ALTER COLUMN store_code    TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date  TYPE DATE,
ALTER COLUMN store_type    TYPE VARCHAR(255),
ALTER COLUMN latitude      TYPE FLOAT,
ALTER COLUMN country_code  TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN continent     TYPE VARCHAR(255);

-- Update latitude where it's null to "N/A"
UPDATE store_details_table
SET latitude = 'N/A'
WHERE latitude IS NULL;
