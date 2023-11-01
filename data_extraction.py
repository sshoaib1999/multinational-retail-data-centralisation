# data_extraction.py

import pandas as pd
import requests
import boto3
import tabula


class DataExtractor:

    def __init__(self, db_connector):
        self.db_connector = db_connector

    def read_rds_table(self, table_name):
        engine = self.db_connector.init_db_engine()
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        return df
    
    def retrieve_pdf_data(self, link):
        # Use tabula to read the PDF into a DataFrame
        # Here, we assume the PDF has tables that tabula can recognize and read
        # We also assume the PDF can have multiple tables across multiple pages, hence pages='all'
        dfs = tabula.read_pdf(link, pages='all', multiple_tables=True)

        # Concatenate all tables into one DataFrame
        df = pd.concat(dfs, ignore_index=True)

    def list_number_of_stores(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()['number_of_stores']  # Assuming the response has a key 'number_of_stores' containing the count
        else:
            return None
        
    def retrieve_stores_data(self, base_endpoint, headers):
        number_of_stores = self.list_number_of_stores("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", headers)
        all_stores = []
        
        for store_number in range(1, number_of_stores + 1):
            endpoint = f"{base_endpoint}/{store_number}"
            response = requests.get(endpoint, headers=headers)
            if response.status_code == 200:
                all_stores.append(response.json())
        
        return pd.DataFrame(all_stores)
    
    @staticmethod
    def _clean_store_data(df):
        # Handle cleaning operations specific to the store data. For example:
        df = df.dropna()  # Drops rows with missing values
        # Add other cleaning steps as necessary...
        
        return df
        
    def extract_from_s3(self, s3_address):
        s3 = boto3.client('s3')
        bucket_name = s3_address.split('//')[1].split('/')[0]
        file_name = s3_address.split('/')[-1]

        try:
            s3.download_file(bucket_name, file_name, file_name)
            df = pd.read_csv(file_name)
            return df
        except Exception as e:
            print(f"An error occurred while downloading and extracting from S3: {e}")
            return None
        
    def extract_and_load_from_s3(self, s3_address, db_connector, table_name):
        s3 = boto3.client('s3')
        bucket_name = s3_address.split('//')[1].split('/')[0]
        file_name = s3_address.split('/')[-1]

        try:
            # Download the JSON file from S3
            s3.download_file(bucket_name, file_name, file_name)

            # Read and parse the JSON data
            df = pd.read_json(file_name)

            # Clean and transform the data (if needed)
            df = self._clean_json_data(df)  # Define your cleaning method

            # Connect to the database
            engine = db_connector.init_db_engine()

            # Insert the cleaned data into the database table
            df.to_sql(table_name, engine, if_exists='replace', index=False)  # Adjust 'if_exists' as needed

            return True
        except Exception as e:
            print(f"An error occurred while downloading, processing, and loading from S3: {e}")
            return False

    def _clean_json_data(self, df):
        # Handle cleaning operations specific to the JSON data. For example:
        df = df.dropna()  # Drops rows with missing values
        # Add other cleaning steps as necessary...
        return df
