import CRUD
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter
from scipy import stats

def do_thi_phan_bo_do_tuoi():
    # Vẽ đồ thị phân bố độ tuổi
    labels = CRUD.age_range['Age_Group']
    sizes = CRUD.age_range['num']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63"]
    # Tạo biểu đồ hình tròn
    plt.figure(figsize=(7, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố độ tuổi')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()
    
def do_thi_CDF_tong_so_mua_hang():
    # TẠO ĐỒ THỊ CDF    
    plt.figure(figsize=(8, 6))
    plt.step(CRUD.sorted_data, CRUD.y, color="red", linestyle='--', linewidth=1)

    # TÙY CHỈNH CỘT X,Y
    plt.xticks(np.arange(0,50, step=5))
    plt.yticks(np.arange(0, 1.1, 0.1))

    # GẮN NHÃN
    plt.xlabel('Tổng số mua hàng')
    plt.ylabel('Phân phối tích lũy')

    # ÁP DỤNG BG
    plt.style.use('ggplot')

    plt.show()
    
# def do_thi_luot_mua_hang():
    
#     # SẮP XẾP DỮ LIỆU
#     sorted_data = np.sort(CRUD.custom_df['Total_Purchases'])

#     # TÍNH TOÁN CDF
#     #Tạo một mảng y với các giá trị từ 1 đến số lượng phần tử trong sorted_data, 
#     #sau đó chia cho tổng số phần tử để tính tỷ lệ tích lũy. Mảng y này thể hiện tỷ lệ phần trăm dữ liệu dưới mỗi giá trị trong sorted_data.
#     y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

#     # TẠO ĐỒ THỊ CDF    
#     plt.figure(figsize=(8, 6))
#     plt.step(sorted_data, y, color="red", linestyle='--', linewidth=1)

#     # TÙY CHỈNH CỘT X,Y
#     plt.xticks(np.arange(0,50, step=5))
#     plt.yticks(np.arange(0, 1.1, 0.1))

#     # GẮN NHÃN
#     plt.xlabel('Tổng số mua hàng')
#     plt.ylabel('Phân phối tích lũy')

#     # ÁP DỤNG BG
#     plt.style.use('ggplot')

#     plt.show()
    
def bieu_do_phan_tich_hinh_thuc_mua_hang():
    # Tạo biểu đồ boxplot
    sns.boxplot(data=CRUD.combined_df, 
                x='Phương thức mua', 
                y='Tổng lượt mua', 
                hue='Phương thức mua', 
                palette='Set2', 
                fliersize=5, 
                linewidth=1, 
                legend=False)

    # Định dạng thêm cho biểu đồ
    plt.xlabel("Phương thức mua")
    plt.ylabel("Tổng lượt mua")
    plt.title("Biểu đồ Boxplot của Tổng lượt mua theo Phương thức mua")
    plt.xticks(rotation=45)  # Xoay nhãn trục x nếu cần
    plt.legend(title='Phương thức mua')  # Hiển thị chú giải nếu muốn
    plt.show()

def do_thi_so_luot_truy_cap_web():
    # Plotting histogram
    plt.hist(CRUD.custom_df['NumWebVisitsMonth'], weights=np.ones(len(CRUD.custom_df['Total_Purchases'])) / len(CRUD.custom_df['Total_Purchases'])*100, bins=5, alpha=0.5, color='pink', edgecolor='darkblue')

    # Customize the y-axis
    plt.gca().yaxis.set_major_formatter(PercentFormatter())

    # Determine the lower value of Total_Purchases
    lower_limit = CRUD.custom_df['NumWebVisitsMonth'].min()

    # Set x-axis limits and ticks
    #plt.xlim(lower_limit, 20)
    plt.xticks(range(lower_limit, 21, 1))


    # Labeling
    plt.xlabel('Số Lần Truy Cập Web')
    plt.ylabel('Phần trăm')

    plt.show()
    
def do_thi_CDF_truy_cap_web():
    # Tạo biểu đồ CDF
    plt.figure(figsize=(8, 6))
    plt.step(CRUD.sorted_purchases, CRUD.y, color="#00AFBB", linestyle='--', linewidth=1)

    # Thiết lập trục x,y
    plt.xticks(np.arange(0,20, step=1))
    plt.yticks(np.arange(0, 1.1, 0.1))

    # Ghi chú trục
    plt.xlabel('Số Lần Truy Cập Web')
    plt.ylabel('Phân phối tích lũy CDF')

    # Thêm BG dang 
    plt.style.use('ggplot')
    # Show the plot
    plt.show()
    #95% khách hàng truy cập website ít hơn 9 lần.
    
def do_thi_dtf_tham_nien_khach_hang():
    sns.set(style="whitegrid")  # Thiết lập phong cách đồ thị là lưới trắng

    # Tạo biểu đồ cột sử dụng seaborn
    sns.barplot(x='Tổng Năm', y='số_lượng', data=CRUD.tham_nien, palette=["#41B7C4", "#CCEDB1", "#F5CA63"])

    # Thêm nhãn văn bản với phần trăm   
    for index, row in CRUD.tham_nien.iterrows():
        plt.text(index, row['số_lượng'], f"{row['số_lượng']} ({row['Phần Trăm']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và tỷ lệ
    plt.xlabel('Số Năm')
    plt.ylabel('Số Lượng')

    # Hiển thị biểu đồ
    plt.show()
    
def do_thi_phan_bo_thoi_gian_gan_bo():
    # Data
    labels = CRUD.tham_nien['Tổng Năm']
    sizes = CRUD.tham_nien['Phần Trăm']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]

    # Create a pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bổ thời gian gắn bó')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()
    
def do_thi_tong_chi_tieu_cac_nam():
    labels = CRUD.grouped_df['Năm Đăng Ký']
    sizes = CRUD.grouped_df['Phần Trăm']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố chi tiêu các năm')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()
    
def hieu_suat_chien_dich():
    sns.set(style="whitegrid")  # Thiết lập phong cách đồ thị là lưới trắng
# Tạo biểu đồ cột sử dụng seaborn
    sns.barplot(x='Offers_Total', y='num', data=CRUD.offers, palette="Set2")
    
    # Thêm nhãn văn bản với phần trăm
    for index, row in CRUD.offers.iterrows():
        plt.text(index, row['num'], f"{row['num']} ({row['percentage']}%)", va='bottom', ha='center')
        
    # Tùy chỉnh nhãn và tỷ lệ
    plt.xlabel('Tổng số ưu đãi')
    plt.ylabel('Số lượng')

    # Hiển thị biểu đồ
    plt.show()

def chien_dich_uu_dai():
    # Thiết lập phong cách biểu đồ
    sns.set(style="whitegrid")

    # Tạo biểu đồ thanh sử dụng seaborn
    sns.barplot(x='Chiến dịch', y='Số Lượng', data=CRUD.df_nhom)

    # Thêm nhãn văn bản với phần trăm
    for index, row in CRUD.df_nhom.iterrows():
        plt.text(index, row['Số Lượng'], f"{row['Số Lượng']} ({row['Phần Trăm']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và thang đo
    plt.xlabel('Chiến dịch')
    plt.ylabel('Số Lượng')
    # Hiển thị biểu đồ
    plt.show()
    
def bieu_do_so_luong_trung_binh_cua_tung_loai_san_pham():
    # Vẽ biểu đồ cột
    plt.figure(figsize=(10, 6))
    CRUD.average_quantities.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Số lượng trung bình của từng loại sản phẩm")
    plt.xlabel("Loại sản phẩm")
    plt.ylabel("Số lượng trung bình")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()