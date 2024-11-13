import pandas as pd
from datetime import date

def remove_null(custom_df):
    custom_df.replace("", pd.NA, inplace=True)
    # xoa cac gia tri con thieu(null)
    custom_df.dropna(inplace= True)
    custom_df.reset_index(drop=True, inplace=True)
    
def update_Education(custom_df):
    custom_df['Education'] = custom_df['Education'].apply(lambda i: 'Master' if i == '2n Cycle' else i)
    # thay hàng có dữ liệu '2n Cycle' thành 'Master'
    
def update_Marital_status(custom_df):
    # Ở cột Marital_Status chỉ giữ lại 2 giá trị là 'Single' và 'In relationship'
    custom_df['Marital_Status'] = custom_df['Marital_Status'].apply(lambda i: 'in relationship' if i == 'Together' or i == 'Married' else i)
    # thay hàng có dữ liệu 'Togethe' và 'Married' thành 'In relationship'
    custom_df['Marital_Status'] = custom_df['Marital_Status'].apply(lambda i: 'Single' if i != 'Single' and i != 'in relationship' else i)
    # thay tất cả các giá trị còn lại thành 'Single'

def delete_columm(custom_df):
    cols_to_drop = ['Kidhome', 'Teenhome', 'Z_CostContact', 'Z_Revenue']
    existing_cols = [col for col in cols_to_drop if col in custom_df.columns]
    if existing_cols:
        custom_df = custom_df.drop(existing_cols, axis=1)

