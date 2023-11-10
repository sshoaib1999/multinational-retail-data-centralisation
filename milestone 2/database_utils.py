import psycopg2
import yaml
from sqlalchemy import create_engine, inspect



class DatabaseConnector:

    def get_engine(self):
        return self.engine
    
    def init_db_connection(self, creds_file):
        credentials = self.read_db_creds(creds_file)
        try:
            conn = psycopg2.connect(
                dbname=credentials['RDS_DATABASE'],
                user=credentials['RDS_USER'],
                password=credentials['RDS_PASSWORD'],
                host=credentials['RDS_HOST'],
                port=credentials['RDS_PORT']
            )
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")
            return None

    def read_db_creds(self, creds_file):
        """
        Read database credentials from a YAML file and return a dictionary.

        Args:
            creds_file (str): Path to the YAML file containing database credentials.

        Returns:
            dict: A dictionary of database credentials.
        """
        try:
            with open(creds_file, 'r') as file:
                credentials = yaml.safe_load(file)
            return credentials
        except Exception as e:
            # Handle exceptions, e.g., if the file is not found or the YAML is incorrectly formatted.
            print(f"Error reading credentials: {str(e)}")
            return {}

    def init_db_engine(self, creds_file):
        """
        Initialize and return an SQLAlchemy database engine using credentials from a YAML file.

        Args:
            creds_file (str): Path to the YAML file containing database credentials.

        Returns:
            sqlalchemy.engine.base.Connection: An SQLAlchemy database engine.
        """
        credentials = self.read_db_creds(creds_file)

        if not credentials:
            return None  # Return None if credentials could not be read

        try:
            db_url = f"postgresql://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}"
            engine = create_engine(db_url)
            return engine
        except Exception as e:
            print(f"Error initializing the database engine: {str(e)}")
            return None

    def list_db_tables(self, engine):
        """
        List all tables in the database.

        Args:
            engine: SQLAlchemy database engine.

        Returns:
            list: A list of table names.
        """
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    def list_db_tables(self, engine):
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        return tables
    
    def __init__(self, database_name, user, password, host, port):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.engine = self.init_db_engine()

    def init_db_engine(self):
        db_url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}'
        engine = create_engine(db_url)
        return engine
    
    def upload_to_db(self, data, table_name):
        """
        Upload a Pandas DataFrame to a database table.

        Args:
            data (pandas.DataFrame): Data to be uploaded.
            table_name (str): Name of the database table to upload to.
        """
        engine = self.init_db_engine()
        with engine.connect() as connection:
            data.to_sql(table_name, connection, if_exists='replace', index=False)

    def connect(self):
        # Add code to establish a database connection
        pass

    def execute_query(self, conn, query):
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None
        
    def close_connection(self, conn):
        if conn:
            conn.close()
            print("Database connection closed")

    def from_yaml(cls, yaml_file):
    # Read database credentials from a YAML file
        with open(yaml_file, 'r') as file:
            creds = yaml.safe_load(file)

    # Create an instance of DatabaseConnector with credentials from the YAML
        return cls(
        database_name=creds['RDS_DATABASE'],
        user=creds['RDS_USER'],
        password=creds['RDS_PASSWORD'],
        host=creds['RDS_HOST'],
        port=creds['RDS_PORT']
    )

# You'll define methods for database connection and data uploading when required.