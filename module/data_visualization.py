import data_connection
import data_cleaning
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
from datetime import date


def bieu_do_phan_tich_muc_do_phan_nan():
     
     # Tạo nhóm độ tuổi
     bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
     #Danh sách tên gọi của các nhóm tuổi tương ứng với các ngưỡng trong bins
     labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
     #Sử dụng hàm cut để phân loại cột age trong tập dữ liệu đã làm sạch 
     #Tạo cột mới là nhóm tuổi dựa trên cột age 
     data_cleaning.custom_df['AgeGroup'] = pd.cut(data_cleaning.custom_df['Age'], bins=bins, labels=labels)
     # Tính số lượng phàn nàn trong từng nhóm tuổi
     grouped_data = data_cleaning.custom_df.groupby(['AgeGroup', 'Complain'], observed=True).size().unstack(fill_value=0)
     # Vẽ biểu đồ cột
     # kind = 'bar' xác định đây là biểu đồ cột
     # stack = true để tạo biểu đồ cột chồng 
     # color để tạo màu cho 2 cột
     grouped_data.plot(kind='bar', stacked=True, color=['lightblue', 'salmon'])
     # đặt tiêu đề cho biểu đồ 
     plt.title('Số lượng phàn nàn theo nhóm tuổi')
     # đặt nhãn lần lươt cho trục x và y
     plt.xlabel('Nhóm tuổi')
     plt.ylabel('Số lượng khách hàng')
     #Đặt góc xoay của nhãn trên trục x thành 0 độ để thể hiện nhãn nhóm tuổi dễ đọc hơn
     plt.xticks(rotation=0)
     # đặt chú giải cho biểu đồ 
     plt.legend(['Không phàn nàn', 'Có phàn nàn'])
     # hàm show để hiện biểu đồ
     plt.show()
def bieu_do_phan_tich_ty_le_chap_nhan_chien_dich_cua_khach_hang():
     # Tính tổng số lần chấp nhận cho từng chiến dịch
     campaign_acceptance = data_cleaning.custom_df[["AcceptedCmp1", "AcceptedCmp2", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5"]].sum()
     # tạo hình ảnh cho  biểu đồ với kích thước 10x10
     plt.figure(figsize=(10, 10))

     plt.bar(campaign_acceptance.index, campaign_acceptance.values, color='skyblue', edgecolor='black')
     #đặt nhãn 
     plt.xlabel("Chiến Dịch")
     plt.ylabel("Số Lượng Khách Hàng Chấp Nhận")
     plt.title("Số Lượng Khách Hàng Chấp Nhận Ưu Đãi Cho Mỗi Chiến Dịch")
     #hiển thị biểu đồ
     plt.show()
def bieu_do_tan_suat_mua_hang_theo_do_tuoi():
    
    # Tính tuổi của khách hàng từ năm sinh cho đến năm hiện tại
    current_year = pd.Timestamp.now().year
    # tạo cột mới tính tuổi bằng cách lấy năm hiện tại trừ đi cột year birth của từng khách hàng
    data_cleaning.custom_df['Age'] = current_year - data_cleaning.custom_df['Year_Birth']
    
    # Phân loại nhóm tuổi bằng cách tạo ra cột mới là AgeGroup
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    #Chia dữ liệu trong cột Age thành các khoảng giá trị (hoặc nhóm) dựa trên các giá trị trong bins và gán nhãn cho #từng nhóm theo danh sách labels.
    data_cleaning.custom_df['AgeGroup'] = pd.cut(data_cleaning.custom_df['Age'], bins=bins, labels=labels)

    # Tính tổng tần suất mua hàng theo nhóm tuổi
    tan_suat_tuoi = data_cleaning.custom_df.groupby('AgeGroup')[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum()

    # Vẽ biểu đồ cột
    tan_suat_tuoi.plot(kind='bar', stacked=True, figsize=(12, 7), edgecolor='black')
    plt.xlabel("Nhóm Tuổi")
    plt.ylabel("Tần Suất Mua Hàng")
    #đặt giới hạn cho cột y
    plt.ylim(0, 10000)
    plt.title("Tần Suất Mua Hàng Qua Các Kênh Theo Nhóm Tuổi")
    plt.legend(["Deals", "Web", "Catalog", "Store"], title="Kênh Mua Hàng")
    plt.xticks(rotation=30)#xoay nhãn trục x 30 độ 
    plt.show()
def bieu_do_tron_phan_tich_hinh_thuc_mua_hang(df = data_cleaning.custom_df): 
    # Tính tổng số lần mua hàng qua các kênh bằng hàm sum
    hinh_thuc_mua_hang = {
        'Deals': df['NumDealsPurchases'].sum(),
        'Web': df['NumWebPurchases'].sum(),
        'Catalog': df['NumCatalogPurchases'].sum(),
        'Store': df['NumStorePurchases'].sum()
    }

    # Vẽ biểu đồ tròn
    plt.figure(figsize=(8, 8))
    plt.pie(hinh_thuc_mua_hang.values(), labels=hinh_thuc_mua_hang.keys(), autopct='%1.1f%%', startangle=0, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title("Tỷ lệ hình thức mua hàng qua các kênh")
    plt.show()

# phần của đăng tường
def bieu_do_the_so_luong_tb_cua_moi_sp():
     #Biểu đồ thanh cho Số lượng trung bình của mỗi loại sản phẩm
    # Chọn các cột sản phẩm liên quan
    product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    # Tính trung bình cho mỗi loại sản phẩm
    data = data_cleaning.custom_df
    average_quantities = data[product_columns].mean()

    # Thiết lập kích thước và vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    average_quantities.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Average Quantity of Each Product Type")
    plt.xlabel("Product Type")
    plt.ylabel("Average Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()  # Tự động điều chỉnh bố cục để biểu đồ không bị cắt
    plt.show()
def bieu_do_phan_bo_do_tuoi():
    # Tạo cột Age dựa trên năm sinh của khách hàng
    data = data_cleaning.custom_df
    current_year = 2024
    data['Age'] = current_year - data['Year_Birth']

    # Đặt các khoảng tuổi và nhãn tương ứng
    bins = [0, 25, 35, 45, 55, 65, 75, 100]
    labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']
    # Phân nhóm khách hàng theo độ tuổi
    data['Age_Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

    # Đếm số lượng khách hàng trong mỗi nhóm tuổi
    age_group_counts = data['Age_Group'].value_counts().sort_index()

    # Vẽ biểu đồ thanh cho phân phối nhóm tuổi
    plt.figure(figsize=(10, 6))
    age_group_counts.plot(kind='bar', color='salmon', edgecolor='black')
    plt.title("Age Group Distribution")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def bieu_do_so_sanh_chi_tieu_va_thu_nhap():
    data = data_cleaning.custom_df
    product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    # So sánh tổng thu nhập và tổng chi tiêu của 50 khách hàng đầu tiên
    # Tính tổng chi tiêu của mỗi khách hàng qua các loại sản phẩm
    data['Total_Expenditure'] = data[product_columns].sum(axis=1)
    # Loại bỏ các hàng thiếu dữ liệu thu nhập
    data = data.dropna(subset=['Income'])
    # Đảm bảo cột Income là kiểu float
    data['Income'] = data['Income'].astype(float)

    # Lấy mẫu dữ liệu 50 khách hàng đầu tiên
    sample_data = data.head(50)

    # Vẽ biểu đồ thanh so sánh thu nhập và chi tiêu
    plt.figure(figsize=(14, 8))
    plt.bar(sample_data.index - 0.2, sample_data['Income'], width=0.4, label='Total Income', color='blue')
    plt.bar(sample_data.index + 0.2, sample_data['Total_Expenditure'], width=0.4, label='Total Expenditure', color='red')
    plt.title('Comparison of Total Income and Total Expenditure (First 50 Customers)')
    plt.xlabel('Customer Index')
    plt.ylabel('Amount')
    plt.legend()
    plt.tight_layout()
    plt.show()
def bieu_do_phan_phoi_luot_truy_cap_web():
    # Lấy cột số lượt truy cập web
    data = data_cleaning.custom_df
    web_visits = data['NumWebVisitsMonth']

    # Vẽ biểu đồ histogram cho phân phối lượt truy cập web
    plt.figure(figsize=(10, 6))
    plt.hist(web_visits, bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Web Visits per Month')
    plt.xlabel('Number of Web Visits in a Month')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
