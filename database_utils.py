# database_utils.py

import yaml
from sqlalchemy import create_engine

class DatabaseConnector:
    
    @staticmethod
    def read_db_creds():
        with open("db_creds.yaml", 'r') as file:
            return yaml.safe_load(file)
    
    def init_db_engine(self):
        creds = self.read_db_creds()
        engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        with engine.connect() as conn:
            return conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'").fetchall()
        
    def upload_to_db(self, df, table_name):
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, index=False, if_exists='replace')



    
