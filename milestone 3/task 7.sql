-- Change data types
ALTER TABLE dim_card_details
ALTER COLUMN card_number            TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN expiry_date            TYPE VARCHAR(?), -- Replace ? with the actual maximum length
ALTER COLUMN date_payment_confirmed TYPE DATE;
