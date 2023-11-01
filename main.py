# main.py

from database_connector import DatabaseConnector
from data_extractor import DataExtractor
from data_cleaning import DataCleaning

def main():
    # Initialization
    db_connector = DatabaseConnector()
    data_extractor = DataExtractor(db_connector)
    headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

    # Extract & Clean Data
    user_data_table_name = [name for name in db_connector.list_db_tables() if 'user' in name][0]
    df = data_extractor.read_rds_table(user_data_table_name)
    df_cleaned = DataCleaning.clean_user_data(df)

    # Upload Cleaned Data
    db_connector.upload_to_db(df_cleaned, "dim_users")

    # Extract Card Data from PDF
    pdf_link = "YOUR_S3_LINK_TO_PDF"  # Replace with the actual S3 link
    df = data_extractor.retrieve_pdf_data(pdf_link)

    # Clean Card Data
    df_cleaned = DataCleaning.clean_card_data(df)

    # Upload Cleaned Data
    db_connector.upload_to_db(df_cleaned, "dim_store_details")

    # Upload Cleaned Data to dim_card_details table
    db_connector.upload_to_db(df_cleaned, "dim_card_details")

     # Extract & Clean Store Data
    df = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details", headers)
    df_cleaned = DataCleaning._clean_store_data(df)

    # Extract Product Data from S3
    s3_address = "s3://data-handling-public/products.csv"  # Replace with the actual S3 address
    df = data_extractor.extract_from_s3(s3_address)
    
    if df is not None:
        # Clean Product Data
        df = DataCleaning.convert_product_weights(df)
        df = DataCleaning.clean_products_data(df)
        
        # Upload Cleaned Data
        db_connector.upload_to_db(df, "dim_products")

    # List all tables in the database
    tables = db_connector.list_db_tables()
    
    # Identify the table containing orders data
    orders_table_name = 'orders'  # Replace with the actual name of the orders table

    # Extract Orders Data
    df_orders = db_connector.read_rds_table(orders_table_name)

    # Clean Orders Data
    df_orders_cleaned = DataCleaning.clean_orders_data(df_orders)

    # Upload Cleaned Orders Data to a New Table
    db_connector.upload_to_db(df_orders_cleaned, "orders_table")


if __name__ == "__main__":
    main()
