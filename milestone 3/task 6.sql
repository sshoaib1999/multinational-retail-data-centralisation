-- Change data types
ALTER TABLE dim_date_times
ALTER COLUMN month       TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN year        TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN day         TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN time_period TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN date_uuid   TYPE UUID;
