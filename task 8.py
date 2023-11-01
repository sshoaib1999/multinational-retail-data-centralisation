import json
import boto3
import psycopg2

# AWS S3 and database connection parameters
aws_access_key_id = 'AKIAV4LULN6J4VDZMPUV'
aws_secret_access_key = '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'
s3_bucket_name = 'multinational-retail-data-centralisation'
s3_object_key = 'date_details.json'
db_host = 'localhost'
db_port = '5432'
db_name = 'sales_data'
db_user = 'postgres'
db_password = 'Smsnn624'

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id='AKIAV4LULN6J4VDZMPUV', aws_secret_access_key='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')

# Download the JSON file from S3
s3.download_file('multinational-retail-data-centralisation', 'date_details.json', 'date_details.json')

# Read and parse the JSON data
with open('date_details.json', 'r') as file:
    json_data = json.load(file)

# Clean and transform the data as needed

# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor for database operations
cur = conn.cursor()

# Create the "dim_date_times" table
create_table_query = """
CREATE TABLE dim_date_times (
    date_column DATE,
    attribute1 VARCHAR(255),
    attribute2 INT
    -- Add more columns as needed
);
"""
cur.execute(create_table_query)

# Insert the cleaned data into the table
insert_query = "INSERT INTO dim_date_times (date_column, attribute1, attribute2) VALUES (%s, %s, %s)"

for record in json_data:
    if isinstance(record, dict):
        date_column = record.get('date_column', None)
        attribute1 = record.get('attribute1', None)
        attribute2 = record.get('attribute2', None)

        if date_column is not None and attribute1 is not None and attribute2 is not None:
            cur.execute(insert_query, (date_column, attribute1, attribute2))

# Commit changes and close the database connection
conn.commit()
conn.close()

# Clean up: Delete the downloaded JSON file
import os
os.remove('date_details.json')
