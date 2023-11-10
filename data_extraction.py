import pandas as pd
from database_utils import DatabaseConnector
import tabula
import requests
import boto3


class DataExtractor:

    def __init__(self, db_connector):
        self.db_connector = db_connector

    def read_rds_data(self, table_name):
        engine = self.db_connector.get_engine()
        # Check if the table name exists in the list of tables
        if table_name not in self.db_connector.list_db_tables(engine):
            raise ValueError(f"Table '{table_name}' does not exist in the database.")

        # Read data from the table using the DatabaseConnector
        engine = self.db_connector.get_engine()
        try:
            connection = engine.connect()
            query = f"SELECT * FROM {table_name}"
            data = pd.read_sql(query, connection)
            connection.close()
            return data
        except Exception as e:
            print(f"Error reading data from the table: {str(e)}")
            return None
        
    def read_rds_table(self, table_name):
        """
        Extract a database table to a Pandas DataFrame.

        Args:
            table_name (str): Name of the table to extract.

        Returns:
            pandas.DataFrame: Data from the specified table.
        """
        # Check if the table name exists in the list of tables
        if table_name not in self.db_connector.list_db_tables():
            raise ValueError(f"Table '{table_name}' does not exist in the database.")

        # Read data from the table using the DatabaseConnector
        engine = self.db_connector.get_engine()
        try:
            data = pd.read_sql_table(table_name, con=engine)
            return data
        except Exception as e:
            print(f"Error reading data from the table: {str(e)}")
            return None
        
    def retrieve_pdf_data(self, pdf_link):
        """
        Extract data from a PDF document and return it as a Pandas DataFrame.

        Args:
            pdf_link (str): Link to the PDF document.

        Returns:
            pandas.DataFrame: Extracted data from the PDF.
        """
        try:
            # Use tabula to extract data from all pages of the PDF
            extracted_data = tabula.read_pdf(pdf_link, pages="all")

            # Combine data from all pages into a single DataFrame
            combined_data = pd.concat(extracted_data, ignore_index=True)

            return combined_data
        except Exception as e:
            print(f"Error extracting data from PDF: {str(e)}")
            return None

    def list_number_of_stores(self, number_of_stores_endpoint, headers):
        try:
            response = requests.get(number_of_stores_endpoint, headers=headers)
            if response.status_code == 200:
                data = response.json()  # Assuming the response is in JSON format
                return data.get('number_of_stores', 0)
            else:
                print(f"Failed to retrieve the number of stores. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error while retrieving the number of stores: {str(e)}")
        return 0  # Return 0 if there's an error

    def retrieve_stores_data(self, retrieve_store_endpoint, headers):
        try:
            response = requests.get(retrieve_store_endpoint, headers=headers)
            if response.status_code == 200:
                data = response.json()  # Assuming the response is in JSON format
                # Assuming the data is a list of stores
                stores_data = pd.DataFrame(data)
                return stores_data
            else:
                print(f"Failed to retrieve store data. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error while retrieving store data: {str(e)}")
        return None  # Return None if there's an error

    def extract_from_s3(self, s3_address):
        try:
            # Initialize an S3 client using AWS CLI credentials
            s3 = boto3.client('s3')

            # Split the S3 address to extract the bucket name and file path
            s3_parts = s3_address.replace("s3://", "").split("/")
            bucket_name = s3_parts[0]
            file_path = "/".join(s3_parts[1:])

            # Download the CSV file from S3
            s3_object = s3.get_object(Bucket=bucket_name, Key=file_path)
            data = s3_object['Body'].read()

            # Convert the data to a Pandas DataFrame
            product_data = pd.read_csv(BytesIO(data))

            return product_data
        except Exception as e:
            print(f"Error extracting data from S3: {str(e)}")
            return None

        

        

# You'll define methods for each data source in this class when required.
