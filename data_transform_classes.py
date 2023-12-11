import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'altered_loan_payments2.csv'
df = pd.read_csv(file_path)


class DataTransforming:
    '''
    This class is used to alter any columns that aren't in the correct format.
    The class handles these conversions.
    '''
    @staticmethod
    def to_numeric(df, columns):
        '''
        This function is used to convert data to integer/float format.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = pd.to_numeric(df[columns], errors='coerce')
        return df

    @staticmethod
    def to_datetime(df, columns):
        '''
        This function is used to convert data to integer/float format.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = df[columns].apply(pd.to_datetime, errors='coerce')
        return df

    @staticmethod
    def to_string(df, columns):
        '''
        This function is used to convert data to string format.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = df[columns].astype(str)
        return df
    
    @staticmethod
    def to_category(df, columns):
        '''
        This function is used to convert data to categroical data type.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = pd.Categorical(df[columns])
        return df

    @staticmethod
    def to_category_codes(df, columns):
        '''
        This function is used to convert data to categroical data type with codes.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = pd.Categorical(df[columns]).codes +1
        return df
    
    @staticmethod
    def to_boolean(df, columns):
        '''
        This function is used to convert data to boolean data type.

        Args:
            df: the dataframe.
            columns: the columns within the dataframe df.
        '''
        df[columns] = df[columns].astype(bool)
        return df

class DataFrameInfo:
    '''
    This class is used to extract information from the DataFrame and its columns.

    Attributes:
        df: the dataframe
    '''
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        """Describe all columns in the DataFrame to check their data types."""
        return self.df.dtypes

    def extract_statistics(self):
        """Extract statistical values: median, standard deviation, and mean from the columns and the DataFrame."""
        return self.df.describe()

    def count_distinct_values(self):
        """Count distinct values in categorical columns."""
        return {col: self.df[col].nunique() for col in self.df.select_dtypes(include='object').columns}

    def print_shape(self):
        """Print out the shape of the DataFrame."""
        print(f"DataFrame shape: {self.df.shape}")

    def null_values_count(self):
        """Generate a count/percentage count of NULL values in each column."""
        null_count = self.df.isnull().sum()
        null_percentage = round((self.df.isnull().sum() / len(self.df)) * 100, 2)
        null_info = pd.DataFrame({'Null Count': null_count, 'Null Percentage': null_percentage})
        return null_info

class Plotter:
    '''
    This class is used to visualise insights from the data.
    '''
    @staticmethod
    def visualize_nulls(data_before_imputation1, data_after_imputation1):
        ''' This function is used to visualise the removal of nulls'''

        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        
        axs[0].set_title('Original Data')
        data_before_imputation1.isnull().sum().plot(kind='bar', ax=axs[0])
        
        axs[1].set_title('Data after NULL Removal')
        data_after_imputation1.isnull().sum().plot(kind='bar', ax=axs[1])
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_skew(data_after_imputation, column_name):
        '''This function is used to visualise the data to check the results of the transformation have improved the skewness of the data'''

        plt.figure(figsize=(6, 4))
        plt.hist(data_after_imputation[column_name], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Skewness: {data_after_imputation[column_name].skew()}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()
    
    def visualize_outliers(self, data):
        '''This function is used to vsiualise if the columns contain outliers'''
        num_cols = data.select_dtypes(include=['float64', 'float32', 'int64', 'int32']).columns
        for col in num_cols:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=data[col])
            plt.title(f'Identifying Outliers in {col}')
            plt.show()
