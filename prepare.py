import pandas as pd
from sklearn.model_selection import train_test_split

import env
import os
import acquire


def prep_telco(df):
    """
    Drops columns 'payment_type_id', 'internet_service_type_id', and 'contract_type_id'
    Takes 'internet_service_type' and fills in all the Null values with None
    Takes away an extra space infront of the data for total_charges
    Adds a zero to toal_charges to allow it to become a type float
    Returns the new prepared data
    """
    df = df.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'])
    df['internet_service_type'] = df['internet_service_type'].fillna('none')
    df.total_charges = df.total_charges.str.replace(' ','0.0')
    df['total_charges'] = (df.total_charges + '0').astype(float)
    return df

def split_data(df, col):
    """
    Takes in dataframe and targer column
    Splits the data into 60% Train and 40% Validate_Test
    Splits the data again from Validate_Test into 50% Validate and 50% Test
    Returns the split data as train, validate, and test
    """
    #first split
    train, validate_test = train_test_split(df,
                train_size = 0.60, 
                random_state = 123, 
                stratify = df[col] 
                )
    
    #second split
    validate, test = train_test_split(validate_test,
                test_size = 0.50,
                random_state = 123,
                stratify = validate_test[col]
                )
    return train, validate, test

def telco_encoded(train, validate, test):
    """
    Starts an empty list as 'encoded_dfs'
    Takes train, validate, and test into the for loop
    Creates a copy of the df under 'df_encoded'
    Runs another for loop in the original pulling every column from each of the dataframes
    If column is 'customer_id' it skips past
    If column is 'total_charges' it skips past
    For the rest of the columns if it's an object it goes through the pd.get_dummies code if not it skips through
    df_dummies takes the column, gives it the same name, drops the first column, and sets it as an int
    df_encoded joins with df_dummies and drops the original column it took the data from'
    df_encoded gets appended into encoded_dfs and gets returned
    """
    encoded_dfs = []
    for df in [train, validate, test]:
        df_encoded = df.copy()
        for col in df.columns:
            if col == 'customer_id':
                continue
            if col == 'total_charges':
                continue
            elif df[col].dtype == 'O':  
                df_dummies = pd.get_dummies(df[col], prefix=col, drop_first=True).astype(int)
                df_encoded = df_encoded.join(df_dummies).drop(columns=[col])
        encoded_dfs.append(df_encoded)
    return encoded_dfs