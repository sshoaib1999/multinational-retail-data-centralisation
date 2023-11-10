import pandas as pd
import re

class DataCleaning:
    def clean_user_data(self, user_data):
        """
        Clean user data by handling NULL values, date errors, incorrectly typed values, and incorrect information.

        Args:
            user_data (pandas.DataFrame): User data to be cleaned.

        Returns:
            pandas.DataFrame: Cleaned user data.
        """
        # Handle NULL values
        user_data.dropna(inplace=True)

        # Handle date errors (if applicable)
        # For example, convert date columns to the correct date format

        # Handle incorrectly typed values and incorrect information
        # You may apply specific data type conversions and filtering logic here

        return user_data
    
    def validate_card_number(card_number):
    # Remove any whitespace or hyphens from the card number
        card_number = card_number.replace(" ", "").replace("-", "")

    # Check if the card number consists of digits and falls within a specified length range
        if card_number.isdigit() and 12 <= len(card_number) <= 19:
            return True
        else:
            return False
    
    def clean_card_data(self, card_data):
        """
        Clean the extracted card data by removing erroneous values, NULL values, or formatting errors.

        Args:
            card_data (pandas.DataFrame): Extracted card data.

        Returns:
            pandas.DataFrame: Cleaned card data.
        """
        # Remove rows with NULL values
        card_data = card_data.dropna()

        # Additional data cleaning steps as needed
        # For example, you can perform formatting checks, remove duplicates, etc.

        # Example: Remove rows with invalid card numbers (you can implement your own validation logic)
        card_data = card_data[card_data['Card Number'].apply(validate_card_number)]

        return card_data
    
    def _clean_store_data(self, store_data):
        if store_data is None:
            return None

        # Example cleaning logic
        cleaned_data = store_data.copy()

        # Remove rows with missing values (NULL)
        cleaned_data.dropna(inplace=True)

        # Clean data type conversions or other cleaning operations

        return cleaned_data
    
    def convert_product_weights(self, products_df):
        try:
            # Create a function to clean and convert weights
            def clean_and_convert_weight(weight):
                if pd.notna(weight):
                    # Remove non-alphanumeric characters and whitespace
                    weight = re.sub(r'[^0-9a-zA-Z.]', '', str(weight))

                    # Define conversion factors for ml and g to kg
                    conversion_factors = {
                        'g': 0.001,
                        'ml': 0.001,
                    }

                    # Extract unit from the weight (e.g., g, ml)
                    unit = re.search(r'[a-zA-Z]+', weight)
                    if unit:
                        unit = unit.group().lower()
                        # Check if the unit is in the conversion factors
                        if unit in conversion_factors:
                            # Convert the weight to kg
                            weight_in_kg = float(re.sub(r'[a-zA-Z]+', '', weight)) * conversion_factors[unit]
                            return weight_in_kg
                    # If no unit is found or unit is not in the conversion factors, return NaN
                    return None
                return None

            # Apply the clean_and_convert_weight function to the weight column
            products_df['weight'] = products_df['weight'].apply(clean_and_convert_weight)

            return products_df
        except Exception as e:
            print(f"Error converting product weights: {str(e)}")
            return None
        
    def clean_products_data(self, products_df):
        try:
            # Clean the DataFrame from additional erroneous values
            # You can perform specific cleaning operations based on your data's requirements here.
            # For example, you can remove rows with missing or invalid values, duplicates, etc.
            # Here's an example of removing rows with missing product names and duplicates based on the 'product_code' column:
            cleaned_products_df = products_df.dropna(subset=['product_name'])
            cleaned_products_df = cleaned_products_df.drop_duplicates(subset=['product_code'])

            return cleaned_products_df
        except Exception as e:
            print(f"Error cleaning products data: {str(e)}")
            return None
        
    def clean_orders_data(self, orders_data):
        """
        Clean the orders data by removing unnecessary columns.

        Args:
            orders_data (pandas.DataFrame): Orders data to be cleaned.

        Returns:
            pandas.DataFrame: Cleaned orders data.
        """
        # Remove the columns 'first_name', 'last_name', and '1'
        columns_to_remove = ['first_name', 'last_name', '1']
        cleaned_orders_data = orders_data.drop(columns=columns_to_remove, errors='ignore')

        return cleaned_orders_data







    def clean_csv_data(self, data):
        # Add code to clean data extracted from CSV
        pass

    def clean_api_data(self, data):
        # Add code to clean data extracted from an API
        pass

    def clean_s3_data(self, data):
        # Add code to clean data extracted from an S3 bucket
        pass

# You'll define methods for data cleaning from each data source when required.