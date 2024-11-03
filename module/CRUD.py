import pandas as pd
from datetime import date


# READ
pd.options.display.max_rows = 9999
pd.options.display.max_columns = 60
df = pd.read_csv('D:/PYTHON/PROJECT/data/marketing_campaign.csv', sep=";")


# tạo một df mới copy dữ liệu từ df
custom_df = df.copy()

# UPDATE

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

# DELETE

# Bỏ một số cot
custom_df = custom_df.drop(['ID', 'Z_CostContact', 'Z_Revenue'], axis=1)

print(custom_df.head())

# CREATE

# Tạo một table mới age_range để thực hiện tính phần trăm độ tuổi
age_range = custom_df.groupby('Age_Group').size().reset_index(name='num')
age_range['percentage'] = (age_range['num'] * 100 / age_range['num'].sum()).round(2)
