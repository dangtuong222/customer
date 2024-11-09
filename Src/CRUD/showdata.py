import pandas as pd
import Data_cleaning as Data_cleaning
import CRUD.Read as Read

def show_all_rows():
    # Read the CSV file
    df = Read.read() 
    # Set display options to show all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    # Display all rows
    print(df)
    
    # Reset display options to default (optional)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth')
