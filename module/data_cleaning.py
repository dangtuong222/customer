from datetime import date
import pandas as pd
import data_connection


# xoa cac gia tri con thieu(null)
data_connection.df.dropna(inplace= True)


custom_df = data_connection.df.copy()
# tạo một df mới copy dữ liệu từ df


custom_df['Education'] = custom_df['Education'].apply(lambda i: 'Master' if i == '2n Cycle' else i)
# thay hàng có dữ liệu '2n Cycle' thành 'Master'


# Ở cột Marital_Status chỉ giữ lại 2 giá trị là 'Single' và 'In relationship'
custom_df['Marital_Status'] = custom_df['Marital_Status'].apply(lambda i: 'in relationship' if i == 'Together' or i == 'Married' else i)
# thay hàng có dữ liệu 'Togethe' và 'Married' thành 'In relationship'
custom_df['Marital_Status'] = custom_df['Marital_Status'].apply(lambda i: 'Single' if i != 'Single' and i != 'in relationship' else i)
# thay tất cả các giá trị còn lại thành 'Single'


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


# Bỏ một số bảng
custom_df = custom_df.drop(['ID', 'Year_Birth', 'Z_CostContact', 'Z_Revenue', 'Complain'], axis=1)

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
