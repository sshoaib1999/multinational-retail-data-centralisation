from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
# Assuming you have already initialized the necessary classes and obtained the cleaned product data

# Insert the cleaned products data into the database table 'dim_products'
table_name = 'dim_products'  # Replace with the desired table name
db_connector.upload_to_db(cleaned_product_data, table_name)
print("Data uploaded to 'dim_products' table in 'sales_data' database")