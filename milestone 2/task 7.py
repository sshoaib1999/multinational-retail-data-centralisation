# Assuming you have already initialized the necessary classes and obtained the engine

# List all tables in the database
tables = db_connector.list_db_tables(engine)
print("Available tables in the database:", tables)

# Assuming you have already initialized the necessary classes and obtained the engine

# Replace 'orders_table' with the actual table name containing order data
table_name = 'orders_table'
orders_data = data_extractor.read_rds_table(db_connector, table_name)

if orders_data is not None:
    print("Orders data:", orders_data)
else:
    print("Failed to read orders data from the table")

# Assuming you have already initialized the necessary classes and obtained the engine

# Clean the orders data
cleaned_orders_data = data_cleaning.clean_orders_data(orders_data)

if cleaned_orders_data is not None:
    print("Cleaned orders data:", cleaned_orders_data)

    # Upload the cleaned data to the 'orders_table' in the 'sales_data' database
    db_connector.upload_to_db(cleaned_orders_data, 'orders_table')
    print("Data uploaded to 'orders_table' in 'sales_data' database")
else:
    print("Failed to clean orders data")

