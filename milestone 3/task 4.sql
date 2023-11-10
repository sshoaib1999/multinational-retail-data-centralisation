-- Add weight_class column
ALTER TABLE products_table
ADD COLUMN weight_class VARCHAR(?); -- Replace ? with the appropriate length

-- Update weight_class based on weight range
UPDATE products_table
SET weight_class = 
  CASE 
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    WHEN weight >= 140 THEN 'Truck_Required'
  END;
