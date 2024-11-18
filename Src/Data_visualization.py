from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter
import CRUD.Read as Read
import Data_cleaning as Data_cleaning

def do_thi_phan_bo_do_tuoi():
    data_ct = Read.read()
    # Tính năm hiện tại, thêm cột 'Age'
    current_year = date.today().year
    data_ct['Age'] = current_year - data_ct['Year_Birth']

    # Phân nhóm cột 'Age'
    data_ct['Age_Group'] = data_ct['Age'].apply(
        lambda x: 
        'Children' if x <= 16 else (
        'Youth' if 17 <= x <= 30 else (
        'Middle Aged' if 30 < x <=  45 else 'Old'
        )
    ))
    # Tính phần trăm độ tuổi
    age_range = data_ct.groupby('Age_Group').size().reset_index(name='num')
    age_range['percentage'] = (age_range['num'] * 100 / age_range['num'].sum()).round(2)

    # Vẽ đồ thị phân bố độ tuổi
    labels = age_range['Age_Group']
    sizes = age_range['num']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63"]
    # Tạo biểu đồ hình tròn
    fig = plt.figure(figsize=(7, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố độ tuổi')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    return fig

def do_thi_so_luot_truy_cap_web():
    data_ct = Read.read()
    # Tính tổng số lần mua hàng của khách hàng
    data_ct['Total_Purchases'] = data_ct['NumDealsPurchases' ] + data_ct['NumWebPurchases'] + data_ct['NumCatalogPurchases'] + data_ct['NumStorePurchases']
    # Đảm bảo không có giá trị NaN trong cột Total_Purchases
    data_ct['Total_Purchases'] = pd.to_numeric(data_ct['Total_Purchases'], errors='coerce')
    # Plotting histogram
    fig = plt.hist(data_ct['NumWebVisitsMonth'], weights=np.ones(len(data_ct['Total_Purchases'])) / len(data_ct['Total_Purchases'])*100, bins=5, alpha=0.5, color='pink', edgecolor='darkblue')

    # Customize the y-axis
    plt.gca().yaxis.set_major_formatter(PercentFormatter())

    # Determine the lower value of Total_Purchases
    lower_limit = data_ct['NumWebVisitsMonth'].min()
    plt.title("Số lượt truy cập Web trong tháng")
    # Set x-axis limits and ticks
    #plt.xlim(lower_limit, 20)
    plt.xticks(range(lower_limit, 21, 1))
    # Labeling
    plt.xlabel('Số Lần Truy Cập Web')
    plt.ylabel('Phần trăm')
    return fig

# def do_thi_phan_bo_thoi_gian_gan_bo():
#     data_ct = Read.read()
#     current_year = date.today().year
#     # Tính năm đăng ký của khách hàng
#     data_ct['Dt_Customer'] = pd.to_datetime(data_ct['Dt_Customer'], errors='coerce')
#     data_ct['Enrollment_Year'] = data_ct['Dt_Customer'].dt.year
#     data_ct['Seniority'] = current_year - data_ct['Enrollment_Year']
#     # Đổi tên cột 'Seniority' thành 'Total_Years' trong DataFrame
#     tham_nien = data_ct[['Seniority']].rename(columns={'Seniority': 'Tổng Năm'})

#     # Nhóm theo 'Tổng Năm' và tính số lượng mỗi nhóm
#     tham_nien = tham_nien.groupby('Tổng Năm').size().reset_index(name='Số Lượng')

#     # Tính phần trăm và làm tròn đến 2 chữ số thập phân
#     tham_nien['Phần Trăm'] = (tham_nien['Số Lượng'] * 100 / tham_nien['Số Lượng'].sum()).round(2)

#     # Chuyển đổi 'Tổng Năm' thành biến phân loại (categorical)
#     tham_nien['Tổng Năm'] = tham_nien['Tổng Năm'].astype('category')
    
#     # Data
#     labels = tham_nien['Tổng Năm']
#     sizes = tham_nien['Phần Trăm']
#     colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]

#     # Create a pie chart
#     fig = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
#     plt.title('Phân bố thời gian gắn bó')
#     plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
#     return fig

def do_thi_tong_chi_tieu_cac_nam():
    data_ct = Read.read()
    # Tính tổng chi tiêu của khách hàng
    data_ct['Total_Spent'] = data_ct['MntWines'] + data_ct['MntFruits'] + data_ct['MntMeatProducts'] + data_ct['MntFishProducts'] + data_ct['MntSweetProducts'] +data_ct['MntGoldProds']
    data_ct['Dt_Customer'] = pd.to_datetime(data_ct['Dt_Customer'], errors='coerce')
    data_ct['Enrollment_Year'] = data_ct['Dt_Customer'].dt.year
    # Nhóm theo 'Enrollment_Year' và tính tổng 'Total_Spent' cho mỗi nhóm
    grouped_df = data_ct.groupby('Enrollment_Year')['Total_Spent'].sum().reset_index()

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    grouped_df['percentage'] = (grouped_df['Total_Spent'] * 100 / grouped_df['Total_Spent'].sum()).round(2)

    # Đổi tên các cột sang tiếng Việt để in kết quả
    grouped_df.columns = ['Năm Đăng Ký', 'Tổng Chi Tiêu', 'Phần Trăm']
    
    labels = grouped_df['Năm Đăng Ký']
    sizes = grouped_df['Phần Trăm']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]
    
    fig = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố chi tiêu các năm')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    return fig

def hieu_suat_chien_dich():
    data_ct = Read.read()
    # Tính tổng số phiếu mua hàng được chấp nhận cho mỗi khách hàng
    data_ct['Total_Offers'] = data_ct['AcceptedCmp1'] + data_ct['AcceptedCmp2'] + data_ct['AcceptedCmp3'] + data_ct['AcceptedCmp4'] + data_ct['AcceptedCmp5']
    # Đổi tên cột 'Total_Offers' thành 'Offers_Total'
    offers = data_ct[['Total_Offers']].rename(columns={'Total_Offers': 'Offers_Total'})

    # Nhóm theo 'Offers_Total' và tính số lượng mỗi nhóm
    offers = offers.groupby('Offers_Total').size().reset_index(name='num')

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    # Chú ý: nên sử dụng tổng của cột 'num' trong DataFrame 'offers' chứ không phải 'seniority'
    offers['percentage'] = (offers['num'] * 100 / offers['num'].sum()).round(2)

    # Chuyển đổi 'Offers_Total' thành biến phân loại (categorical)
    offers['Offers_Total'] = offers['Offers_Total'].replace({0: 'Chiến dịch 1', 1: 'Chiến dịch 2', 2: 'Chiến dịch 3', 3: 'Chiến dịch 4', 4: 'Chiến dịch 5'})
    
    sns.set(style="whitegrid")  # Thiết lập phong cách đồ thị là lưới trắng
    # Tạo biểu đồ cột sử dụng seaborn
    fig = sns.barplot(x='Offers_Total', y='num', data=offers, palette="Set2")

    # Thêm nhãn văn bản với phần trăm
    for index, row in offers.iterrows():
        plt.text(index, row['num'], f"{row['num']} ({row['percentage']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và tỷ lệ
    plt.xlabel('Các chiến dịch')
    plt.ylabel('Số lượng')
    plt.title("Hiệu suất chiến dịch")
    # Hiển thị biểu đồ
    return fig

def so_khach_hang_chap_nhan_uu_dai():
    data_ct = Read.read()
    # Tính tổng số phiếu mua hàng được chấp nhận cho mỗi khách hàng
    data_ct['Total_Offers'] = data_ct['AcceptedCmp1'] + data_ct['AcceptedCmp2'] + data_ct['AcceptedCmp3'] + data_ct['AcceptedCmp4'] + data_ct['AcceptedCmp5']
    
    cmp_df = data_ct[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']]
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
    
    # Thiết lập phong cách biểu đồ
    sns.set(style="whitegrid")

    # Tạo biểu đồ thanh sử dụng seaborn
    fig = sns.barplot(x='Chiến dịch', y='Số Lượng', data=df_nhom)

    # Thêm nhãn văn bản với phần trăm
    for index, row in df_nhom.iterrows():
        plt.text(index, row['Số Lượng'], f"{row['Số Lượng']} ({row['Phần Trăm']}%)", va='bottom', ha='center')
    plt.title("Số lượng khách hàng chấp nhận ưu đãi")
    # Tùy chỉnh nhãn và thang đo
    plt.xlabel('Chiến dịch')
    plt.ylabel('Số Lượng')
    # Hiển thị biểu đồ
    return fig

def so_luong_trung_binh_cua_moi_san_pham():
    data_ct = Read.read()
    # Chọn các cột sản phẩm liên quan
    product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    # Tính trung bình cho mỗi loại sản phẩm
    average_quantities = data_ct[product_columns].mean()

    # Thiết lập kích thước và vẽ biểu đồ
    fig = plt.figure(figsize=(10, 6))
    average_quantities.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Số Lượng Trung Bình của Mỗi Loại Sản Phẩm")
    plt.xlabel("Loại sản phẩm")
    plt.ylabel("Số Lượng Trung Bình")
    # điều chỉnh độ nghiêng để các mục ko bị chồng tên 
    plt.xticks(rotation=45)
    plt.tight_layout()  # Tự động điều chỉnh bố cục để biểu đồ không bị cắt
    return fig

# def so_sanh_thu_nhap_va_chi_tieu_50_khach_dau_tien():
#     data_ct = Read.read()
#     # Chọn các cột sản phẩm liên quan
#     product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

#     # Tính tổng chi tiêu của mỗi khách hàng qua các loại sản phẩm
#     data_ct['Total_Expenditure'] = data_ct[product_columns].sum(axis=1)

#     # Loại bỏ các hàng thiếu dữ liệu thu nhập để đảm bảo tính chính xác khi vẽ biểu đồ
#     data_ct = data_ct.dropna(subset=['Income'])

#     # Đảm bảo cột Income là kiểu float để sử dụng cho việc vẽ biểu đồ
#     data_ct['Income'] = data_ct['Income'].astype(float)

#     # Lấy mẫu dữ liệu 50 khách hàng đầu tiên
#     sample_data = data_ct.head(50)

#     # Vẽ biểu đồ đường so sánh thu nhập và chi tiêu
#     fig = plt.figure(figsize=(14, 8))

#     # Vẽ đường cho thu nhập
#     plt.plot(sample_data.index, sample_data['Income'], label='Tổng thu nhập', color='blue', marker='o', linestyle='-', linewidth=2)

#     # Vẽ đường cho chi tiêu
#     plt.plot(sample_data.index, sample_data['Total_Expenditure'], label='Tổng chi tiêu', color='red', marker='o', linestyle='-', linewidth=2)

#     # Thiết lập tiêu đề và nhãn trục
#     plt.title('So sánh Tổng Thu Nhập và Tổng Chi Tiêu (50 Khách Hàng Đầu Tiên)', fontsize=16)
#     plt.xlabel('Chỉ Số Khách Hàng', fontsize=14)
#     plt.ylabel('Giá trị (dvtt)', fontsize=14)
#     # Hiển thị legend
#     plt.legend()
#     # Đảm bảo các thành phần không bị chồng chéo
#     plt.tight_layout()
#     return fig

def bieu_do_phan_tich_muc_do_phan_nan():
    data_ct = Read.read()
    # Tính năm hiện tại, thêm cột 'Age'
    current_year = date.today().year
    # tạo cột age để lưu tuổi của từng khách hàng
    data_ct['Age'] = current_year - data_ct['Year_Birth']
    # Tạo nhóm độ tuổi
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    # Danh sách tên gọi của các nhóm tuổi tương ứng với các ngưỡng trong bins
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    # Sử dụng hàm cut để phân loại cột age trong tập dữ liệu đã làm sạch 
    # Tạo cột mới là nhóm tuổi dựa trên cột age 
    data_ct['AgeGroup'] = pd.cut(data_ct['Age'], bins=bins, labels=labels)
    # Tính số lượng phàn nàn trong từng nhóm tuổi
    # Sử dụng Groupby để nhóm dữ liệu theo AgeGroup, Complain sau đó dùng size() để tính số lượng hàng được tạp bởi grouby() nghĩa là đếm số khách hàng trong mỗi nhóm 
    # unstack để chuyển kết quả từ groupby sang table sử dụng complain làm cột
    grouped_data = data_ct.groupby(['AgeGroup', 'Complain'], observed=True).size().unstack(fill_value=0)
    # Vẽ biểu đồ cột
    # kind = 'bar' xác định đây là biểu đồ cột
    # stack = true để tạo biểu đồ cột chồng 
    # color để tạo màu cho 2 cột
    fig = grouped_data.plot(kind='bar', stacked=True, color=['lightblue', 'salmon'])
    # đặt tiêu đề cho biểu đồ 
    plt.title('Số lượng phàn nàn theo nhóm tuổi')
    # đặt nhãn lần lươt cho trục x và y
    plt.xlabel('Nhóm tuổi')
    plt.ylabel('Số lượng khách hàng')
    #Đặt góc xoay của nhãn trên trục x thành 0 độ để thể hiện nhãn nhóm tuổi dễ đọc hơn
    plt.xticks(rotation=0)
    # đặt chú giải cho biểu đồ 
    plt.legend(['Không phàn nàn', 'Có phàn nàn'])
    return fig

def bieu_do_tan_suat_mua_hang_theo_do_tuoi():
    # Tạo biến data_ct để đọc dữ liệu từ dữ liệu đã làm sạch trong phần crud dưới dạng dataFrame 
    data_ct = Read.read()
    
    # Tính tuổi của khách hàng từ năm sinh cho đến năm hiện tại
    current_year =  date.today().year
    # tạo cột mới tính tuổi bằng cách lấy năm hiện tại trừ đi cột year birth của từng khách hàng
    data_ct['Age'] = current_year - data_ct['Year_Birth']
    
    # Phân loại nhóm tuổi bằng cách tạo ra cột mới là AgeGroup
    # Định nghĩa các nhóm tuổi và nhãn tương ứng của chúng dựa vào 2 list bín và labels
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    # Sử dụng hàm cut() để phân loại dữ liệu từ cột age dựa trên các giá trị được thiết lập trong bins. Dòng lệnh này trẻ về các nhóm mà nhãn của chúng sẽ tương ứng với labels ban đầu 
    data_ct['AgeGroup'] = pd.cut(data_ct['Age'], bins=bins, labels=labels)

    # Tính tổng tần suất mua hàng theo nhóm tuổi
    # Sử dụng grouby() để nhóm các hàng có cùng nhóm tuổi lại 
    # chọn ra các cột cần tính để tính tổng bằng sum()
    # biến tan_suat_tuoi sẽ chứa dataFrame mà trong đó sẽ chứa tổng số lần mua hàng của mỗi hình thức ứng với từng nhóm tuổi
    tan_suat_tuoi = data_ct.groupby('AgeGroup')[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum()

    # Vẽ biểu đồ cột
    # các tham số đầu vào lần lượt như kind để thiết lập loại biểu đồ, stacked để cho biết đây là biểu đồ cột chồng, figsize thể hiện kích thước, edgecolor thể hiện viền của cột
    fig = tan_suat_tuoi.plot(kind='bar', stacked=True, figsize=(12, 7), edgecolor='black')

    plt.xlabel("Nhóm Tuổi")
    plt.ylabel("Tần Suất Mua Hàng")
    #đặt giới hạn cho cột y
    plt.ylim(0, 10000)
    plt.title("Tần Suất Mua Hàng Qua Các Kênh Theo Nhóm Tuổi")
    plt.legend(["Deals", "Web", "Catalog", "Store"], title="Kênh Mua Hàng")
    plt.xticks(rotation=30)#xoay nhãn trục x 30 độ 
    return fig
