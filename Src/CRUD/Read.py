import pandas as pd
from Data_cleaning import remove_null, update_Education, update_Marital_status, delete_columm
    
def read():
    pd.options.display.max_rows = 9999
    pd.options.display.max_columns = 60
    df = pd.read_csv('D:/python/customer/data/marketing_campaign.csv', sep=";", index_col=False)
    remove_null(df)
    update_Education(df)
    update_Marital_status(df)
    df = delete_columm(df)
    return df
def save_file(df):
    df.to_csv('D:/python/customer/data/marketing_campaign.csv', sep=";", index=False)