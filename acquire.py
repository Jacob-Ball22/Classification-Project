import pandas as pd
import env
import os

#The function get_telco_data() gets the telco data from the CodeUp MySQL database

def get_telco_data():
    filename = 'telco.csv'
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        url = env.get_db_url('telco_churn')
        df = pd.read_sql('''select * from customers 
    join contract_types ct
		using (contract_type_id)
	join internet_service_types ist
		using (internet_service_type_id)
	join payment_types pt
		using (payment_type_id)''', url)
        #save to csv
        df.to_csv(filename)
    return df