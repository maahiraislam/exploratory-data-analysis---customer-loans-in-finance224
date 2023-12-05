import yaml
from sqlalchemy import create_engine
import pandas as pd

with open('credentials.yaml','r') as file:
    yaml_dict = yaml.safe_load(file)
#print(yaml_dict)


class RDSDatabaseConnector:
    def __init__(self,yaml_dict):
        self.yaml_dict = yaml_dict
    
    def init_db_engine(self):
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{yaml_dict['RDS_USER']}:{yaml_dict['RDS_PASSWORD']}@{yaml_dict['RDS_HOST']}:{yaml_dict['RDS_PORT']}/{yaml_dict['RDS_DATABASE']}")
        return engine
    
    def extract_loan_payments_data(self):
        using_engine = self.init_db_engine()
        data_frame = pd.read_sql_query('SELECT * FROM loan_payments',using_engine)
        return data_frame
    
    def save_as_csv(self,data_frame):
        data_frame.to_csv('C:/Users/maahi/EDA Project/loan_payments.csv')

connector = RDSDatabaseConnector(yaml_dict)
#print(connector.extract_loan_payments_data())
df = connector.extract_loan_payments_data()
connector.save_as_csv(df)