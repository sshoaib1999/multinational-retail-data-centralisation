from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Assuming you have cleaned store data as 'cleaned_store_data'
table_name = 'dim_store_details'
db_connector = DatabaseConnector(database_name='sales_data', user='postgres', password='Smsnn624', host='localhost', port='5432')
db_connector.upload_to_db(cleaned_store_data, table_name)