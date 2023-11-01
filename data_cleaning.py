# data_cleaning.py

import numpy as np


class DataCleaning:

    @staticmethod
    def clean_user_data(df):
        # Handle NULL values (for this example, we fill them with NaN)
        df = df.replace({None: np.nan})

        # Convert date columns to datetime type (replace 'your_date_column' with the actual column name)
        df['your_date_column'] = pd.to_datetime(df['your_date_column'], errors='coerce')

        # Handle other data cleaning steps as needed...

        return df
    
    @staticmethod
    def clean_card_data(df):
        # Replace NULL values with NaN (or handle them appropriately)
        df = df.replace({None: np.nan, 'NULL': np.nan})

        # Add specific cleaning steps, such as:
        # - Formatting corrections
        # - Data type conversions
        # - Removal of erroneous values
        # Note: This is a generic placeholder. Actual steps would depend on the nature of the data and its anomalies.

        return df
    
    @staticmethod
    def convert_product_weights(df):
        def convert_weight(weight):
            if isinstance(weight, str):
                weight = weight.strip()
                if weight.endswith("ml"):
                    # Assuming a rough 1:1 conversion from ml to g
                    weight = float(weight[:-2]) / 1000  # Convert to kg
                elif weight.endswith("g"):
                    weight = float(weight[:-1]) / 1000  # Convert to kg
                try:
                    return float(weight)
                except ValueError:
                    return None
            return weight

        df['weight'] = df['weight'].apply(convert_weight)
        return df
    
    @staticmethod
    def clean_products_data(df):
        # Add other cleaning steps as necessary
        # For example, removing rows with missing values
        df = df.dropna()
        return df
    
    @staticmethod
    def clean_orders_data(df):
        # Remove unnecessary columns
        df = df.drop(columns=['first_name', 'last_name', '1'])
        
        # You can add additional cleaning steps specific to the orders data here

        return df
    
    
    

    
