# Import necessary classes
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Initialize the DatabaseConnector, DataExtractor, and DataCleaning classes
db_connector = DatabaseConnector.from_yaml(DatabaseConnector, yaml_file='db_creds.yaml')
data_extractor = DataExtractor(db_connector)
data_cleaner = DataCleaning()

# Initialize the database engine
engine = db_connector.init_db_engine()

if engine:
    # Read user data from the database (replace 'legacy_users' with the actual table name)
    user_data = data_extractor.read_rds_data('legacy_users')

    # Clean the user data
    cleaned_user_data = data_cleaner.clean_user_data(user_data)

    if cleaned_user_data is not None:
        print("Cleaned user data:", cleaned_user_data)

        # Upload the cleaned data to the 'dim_users' table in 'sales_data' database
        db_connector.upload_to_db(cleaned_user_data, 'dim_users')
        print("Data uploaded to 'dim_users' table in 'sales_data' database")
    else:
        print("Failed to clean user data")
else:
    print("Failed to initialize the database engine")


