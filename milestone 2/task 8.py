# Assuming you have already initialized the necessary classes and obtained the engine

# Extract data from the S3 link
s3_bucket = 'data-handling-public'
s3_key = 'date_details.json'
date_times_data = data_extractor.extract_from_s3(s3_bucket, s3_key)

# Perform any necessary cleaning (if required)

# Upload the cleaned data to the 'dim_date_times' table in the 'sales_data' database
db_connector.upload_to_db(date_times_data, 'dim_date_times')
print("Data uploaded to 'dim_date_times' in 'sales_data' database")