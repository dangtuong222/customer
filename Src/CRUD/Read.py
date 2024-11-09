import pandas as pd
import Data_cleaning as Data_cleaning
    
def read():
    pd.options.display.max_rows = 9999
    pd.options.display.max_columns = 60
    df = pd.read_csv('D:/Python_project/customer/data/marketing_campaign.csv', sep=";")
    Data_cleaning.remove_null(df)
    Data_cleaning.update_Education(df)
    Data_cleaning.update_Marital_status(df)
    Data_cleaning.delete_columm(df)
    Data_cleaning.updateFrame(df)
    return df
def save_file(df):
    df.to_csv('D:/Python_project/customer/data/marketing_campaign.csv', sep=";")