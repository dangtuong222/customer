import pandas as pd
from datetime import date
import numpy as np

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

# Bỏ một số cột
custom_df = custom_df.drop(['ID', 'Z_CostContact', 'Z_Revenue'], axis=1)

print(custom_df.head())

# CREATE

    # << Phân bố độ tuổi: >>
# Tạo một table mới age_range để thực hiện tính phần trăm độ tuổi
age_range = custom_df.groupby('Age_Group').size().reset_index(name='num')
age_range['percentage'] = (age_range['num'] * 100 / age_range['num'].sum()).round(2)

    # << CDF tổng số mua hàng: >>
# Sắp xếp dữ liệu
sorted_data = np.sort(custom_df['Total_Purchases'])
# Tính toán CDF
#Tạo một mảng y với các giá trị từ 1 đến số lượng phần tử trong sorted_data, 
#sau đó chia cho tổng số phần tử để tính tỷ lệ tích lũy. Mảng y này thể hiện tỷ lệ phần trăm dữ liệu dưới mỗi giá trị trong sorted_data.
y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

    # << Phân tích hình thức mua hàng: >>
# Giả sử bạn có DataFrame tên là custom_df
# Chọn các cột chứa cả 'Num' và 'Purchases' trong tên cột
purchase_columns = [col for col in custom_df.columns if 'Num' in col and 'Purchases' in col]
purchase_df = custom_df[purchase_columns]

# Làm phẳng DataFrame thành danh sách và tạo DataFrame mới với tên phương thức mua lặp lại
total_purchases = purchase_df.values.flatten()
purchase_names = ['Deal', 'Web', 'Catalog', 'Store'] * (len(total_purchases) // 4)

# Tạo DataFrame cho Phương thức mua và Tổng lượt mua
combined_df = pd.DataFrame({
    'Phương thức mua': purchase_names,
    'Tổng lượt mua': total_purchases
})

    # << CDF truy cập web: >>
# Sắp xếp
sorted_purchases = np.sort(custom_df['NumWebVisitsMonth'])
# Tính CDF
y = np.arange(1, len(sorted_purchases) + 1) / len(sorted_purchases)

    # << Thâm niên khách hàng, phân bố thời gian gắn bó: >>
# Đổi tên cột 'Seniority' thành 'Total_Years' trong DataFrame
tham_nien = custom_df[['Seniority']].rename(columns={'Seniority': 'Tổng Năm'})
# Nhóm theo 'Tổng Năm' và tính số lượng mỗi nhóm
tham_nien = tham_nien.groupby('Tổng Năm').size().reset_index(name='số_lượng')
# Tính phần trăm và làm tròn đến 2 chữ số thập phân
tham_nien['Phần Trăm'] = (tham_nien['số_lượng'] * 100 / tham_nien['số_lượng'].sum()).round(2)
# Chuyển đổi 'Tổng Năm' thành biến phân loại (categorical)
tham_nien['Tổng Năm'] = tham_nien['Tổng Năm'].astype('category')
    
    #  << Tổng chi tiêu các năm: >>
# Nhóm theo 'Enrollment_Year' và tính tổng 'Total_Spent' cho mỗi nhóm
grouped_df = custom_df.groupby('Enrollment_Year')['Total_Spent'].sum().reset_index()
# Tính phần trăm và làm tròn đến 2 chữ số thập phân
grouped_df['percentage'] = (grouped_df['Total_Spent'] * 100 / grouped_df['Total_Spent'].sum()).round(2)
# Đổi tên các cột sang tiếng Việt để in kết quả
grouped_df.columns = ['Năm Đăng Ký', 'Tổng Chi Tiêu', 'Phần Trăm']

    # << Hiệu suất chiến dịch: >>
# Đổi tên cột 'Total_Offers' thành 'Offers_Total'
offers = custom_df[['Total_Offers']].rename(columns={'Total_Offers': 'Offers_Total'})
# Nhóm theo 'Offers_Total' và tính số lượng mỗi nhóm
offers = offers.groupby('Offers_Total').size().reset_index(name='num')
# Tính phần trăm và làm tròn đến 2 chữ số thập phân
# Chú ý: nên sử dụng tổng của cột 'num' trong DataFrame 'offers' chứ không phải 'seniority'
offers['percentage'] = (offers['num'] * 100 / offers['num'].sum()).round(2)
# Chuyển đổi 'Offers_Total' thành biến phân loại (categorical)
offers['Offers_Total'] = offers['Offers_Total'].astype('category')

    # << Chiến dịch ưu đãi: >>
# Giả sử custom_df đã được định nghĩa
cmp_df = custom_df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']]
# Kiểm tra số lượng khách hàng
num_customers = cmp_df.shape[0]
# Tạo cột Campaign
Campaign = pd.DataFrame({'Chiến dịch': ['Chiến dịch 1', 'Chiến dịch 2', 'Chiến dịch 3', 'Chiến dịch 4', 'Chiến dịch 5'] * num_customers})
# Tạo cột No_Of_Offers
No_Of_Offers = pd.DataFrame({'Số lượt ưu đãi': cmp_df.values.flatten()})
# Kết hợp Campaign và No_Of_Offers vào cmp_df
cmp_df = pd.concat([Campaign, No_Of_Offers], axis=1)
# Lọc các hàng mà Số Lượng Ưu Đãi bằng 1
df_loc = cmp_df[cmp_df['Số lượt ưu đãi'] == 1]
# Nhóm theo Chiến Dịch và tính số lượng hàng trong mỗi nhóm
df_nhom = df_loc.groupby('Chiến dịch').size().reset_index(name='Số Lượng')
# Tính phần trăm
df_nhom['Phần Trăm'] = (df_nhom['Số Lượng'] * 100 / df_nhom['Số Lượng'].sum()).round(2)
# Nhóm dữ liệu khách hàng theo 'Total_Offers' và tính giá trị trung vị của 'Income'
result_df = custom_df.groupby('Total_Offers').agg(avg_spend=('Income', 'median')).reset_index().round(0)
result_df.columns = ['Tổng Số Ưu Đãi', 'Chi Tiêu TB']

    # << Số lượng trung bình của từng loại sản phẩm: >>
product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
# Tính số lượng trung bình của từng loại sản phẩm
average_quantities = custom_df[product_columns].mean()