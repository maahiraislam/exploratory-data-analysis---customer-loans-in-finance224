import pandas as pd
import yaml
from sqlalchemy import create_engine


with open('credentials.yaml','r') as file:
    yaml_dict = yaml.safe_load(file)
# print(yaml_dict)


class RDSDatabaseConnector:
    '''
    This class is used to extract data from the AWS RDS Database.
    Attributes:
        yaml_dict (dictionary): Contains the database credentials to connect to the remote database
    '''

    def __init__(self,yaml_dict):
        '''
        See help(RDSDataBaseConnector) for accurate signature
        '''
        self.yaml_dict = yaml_dict

    def initialise_database_engine(self):
        '''
        This function initalises an engine from the credentials.

        Returns:
           Object representation
        '''
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{yaml_dict['RDS_USER']}:{yaml_dict['RDS_PASSWORD']}@{yaml_dict['RDS_HOST']}:{yaml_dict['RDS_PORT']}/{yaml_dict['RDS_DATABASE']}")
        return engine
    

    def extract_loan_payments_data(self):
        '''
        This function extracts  data from the RDS database and returns it as a Pandas DataFrame.

        Returns:
            Tabular Data structure with labelled axes
        '''
        using_engine = self.initialise_database_engine()
        data_frame = pd.read_sql_query('SELECT * FROM loan_payments',using_engine)
        return data_frame

    def save_as_csv(self,data_frame):
        '''
        This function saves the data in .csv format.

        Returns:
            Saves DataFrame to filepath
        '''
        data_frame.to_csv('C:/Users/maahi/EDA Project/loan_payments.csv')

connector = RDSDatabaseConnector(yaml_dict)
#print(connector.extract_loan_payments_data())
df = connector.extract_loan_payments_data()
connector.save_as_csv(df)
