#----------------------------
# UTILS
#----------------------------

import pandas as pd
from datetime import date

    
def read_csv_file(file_path: str):
    print('Reading CSV file')
    
    df = pd.read_csv(file_path)

    return df

def get_file_name():
    print("Inside 'UTILS' FILE..!!")

def get_datetime():
    return date.today()