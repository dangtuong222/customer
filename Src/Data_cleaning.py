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
    cols_to_drop = ['ID', 'Kidhome', 'Teenhome', 'Z_CostContact', 'Z_Revenue']
    existing_cols = [col for col in cols_to_drop if col in custom_df.columns]
    if existing_cols:
        custom_df = custom_df.drop(existing_cols, axis=1)

def updateFrame(custom_df):
    # Tính năm hiện tại, thêm cột 'Age'
    current_year = date.today().year
    custom_df['Age'] = current_year - custom_df['Year_Birth']

    # Phân nhóm cột 'Age'
    custom_df['Age_Group'] = custom_df['Age'].apply(
        lambda x: 
        'Children' if x <= 16 else (
        'Youth' if 17 <= x <= 30 else (
        'Middle Aged' if 30 < x <=  45 else 'Old'
        )
    ))
    # Tính tổng chi tiêu của khách hàng
    custom_df['Total_Spent'] = custom_df['MntWines'] + custom_df['MntFruits'] + custom_df['MntMeatProducts'] + custom_df['MntFishProducts'] + custom_df['MntSweetProducts'] +custom_df['MntGoldProds']

    # Tính tổng số lần mua hàng của khách hàng
    custom_df['Total_Purchases'] = custom_df['NumDealsPurchases' ] + custom_df['NumWebPurchases'] + custom_df['NumCatalogPurchases'] + custom_df['NumStorePurchases']
    # Đảm bảo không có giá trị NaN trong cột Total_Purchases
    custom_df['Total_Purchases'] = pd.to_numeric(custom_df['Total_Purchases'], errors='coerce')


    # Tính năm đăng ký của khách hàng
    custom_df['Dt_Customer'] = pd.to_datetime(custom_df['Dt_Customer'], errors='coerce')
    custom_df['Enrollment_Year'] = custom_df['Dt_Customer'].dt.year
    custom_df['Seniority'] = current_year - custom_df['Enrollment_Year']

    # Tính tổng số phiếu mua hàng được chấp nhận cho mỗi khách hàng
    custom_df['Total_Offers'] = custom_df['AcceptedCmp1'] + custom_df['AcceptedCmp2'] + custom_df['AcceptedCmp3'] + custom_df['AcceptedCmp4'] + custom_df['AcceptedCmp5']
    # print(custom_df.head())
