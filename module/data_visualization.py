import data_connection
import data_cleaning
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
from datetime import date

# Biểu đồ phân tích muc độ phàn nàn của khách hàng thông qua độ tuổi 
# Biểu đồ histogram nhiều cột
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
    """
    Vẽ biểu đồ cột thể hiện tần suất mua hàng của khách hàng dựa vào độ tuổi.
    
    Tham số:
    df (DataFrame): DataFrame chứa dữ liệu khách hàng với các cột về tần suất mua hàng
                    ('NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases')
                    và một cột 'Year_Birth' để tính toán độ tuổi.
    """
    # Tính tuổi của khách hàng từ năm sinh
    current_year = pd.Timestamp.now().year
    data_cleaning.custom_df['Age'] = data_cleaning.current_year - data_cleaning.custom_df['Year_Birth']
    
    # Phân loại nhóm tuổi
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    data_cleaning.custom_df['AgeGroup'] = pd.cut(data_cleaning.custom_df['Age'], bins=bins, labels=labels)

    # Tính tổng tần suất mua hàng theo nhóm tuổi
    tan_suat_tuoi = data_cleaning.custom_df.groupby('AgeGroup')[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum()

    # Vẽ biểu đồ cột
    tan_suat_tuoi.plot(kind='bar', stacked=True, figsize=(12, 7), edgecolor='black')
    plt.xlabel("Nhóm Tuổi")
    plt.ylabel("Tần Suất Mua Hàng")
    plt.title("Tần Suất Mua Hàng Qua Các Kênh Theo Nhóm Tuổi")
    plt.legend(["Deals", "Web", "Catalog", "Store"], title="Kênh Mua Hàng")
    plt.xticks(rotation=45)
    plt.show()
def bieu_do_tron_phan_tich_hinh_thuc_mua_hang(df = data_cleaning.custom_df):
    """
    Vẽ biểu đồ tròn để phân tích tỷ lệ hình thức mua hàng của khách hàng qua các kênh mua sắm.
    
    Tham số:
    df (DataFrame): DataFrame chứa dữ liệu khách hàng với các cột tần suất mua hàng qua các kênh
                    ('NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases').
    """
    # Tính tổng số lần mua hàng qua các kênh
    hinh_thuc_mua_hang = {
        'Deals': df['NumDealsPurchases'].sum(),
        'Web': df['NumWebPurchases'].sum(),
        'Catalog': df['NumCatalogPurchases'].sum(),
        'Store': df['NumStorePurchases'].sum()
    }

    # Vẽ biểu đồ tròn
    plt.figure(figsize=(8, 8))
    plt.pie(hinh_thuc_mua_hang.values(), labels=hinh_thuc_mua_hang.keys(), autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title("Tỷ Lệ Hình Thức Mua Hàng Qua Các Kênh")
    plt.show()
