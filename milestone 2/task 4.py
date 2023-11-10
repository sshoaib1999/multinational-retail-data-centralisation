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
    # Retrieve card data from the PDF document (replace 'pdf_link' with the actual link)
    pdf_link = 'https://example.com/your.pdf'  # Replace with the actual PDF link
    card_data = data_extractor.retrieve_pdf_data(pdf_link)

    if card_data is not None:
        # Clean the card data
        cleaned_card_data = data_cleaner.clean_card_data(card_data)

        if cleaned_card_data is not None:
            # Upload the cleaned data to the "dim_card_details" table in the database
            db_connector.upload_to_db(cleaned_card_data, 'dim_card_details')
            print("Data uploaded to 'dim_card_details' table in the database")
        else:
            print("Failed to clean card data")
    else:
        print("Failed to retrieve card data from the PDF")
else:
    print("Failed to initialize the database engine")
