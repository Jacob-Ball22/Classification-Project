import pandas as pd
from sklearn.model_selection import train_test_split

import env
import os
import acquire


def prep_and_split_telco(telco_df, col):
    """
    Drops columns 'payment_type_id', 'internet_service_type_id', and 'contract_type_id'
    Recieves dataframe as 'df' and target variable to stratify as 'col'
    First split does a 60% train and 40% validate
    Second split uses the 40% validate to make 50% validate and 50% test
    """
    telco_df = telco_df.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'])
    #first split
    train, validate_test = train_test_split(telco_df, #send in initial df
                train_size = 0.60, #size of the train df, and the test size will default to 1-train_size
                random_state = 123, #set any number here for consistency
                stratify = telco_df[col] #we should stratify on our target variable
                )
    
    #second split
    validate, test = train_test_split(validate_test, #we are spliting the 40% df we just made
                test_size = 0.50, #split 50/50
                random_state = 123, #gotta send in a random seed
                stratify = validate_test[col] #still got to stratify
                )
    
    return train, validate, test