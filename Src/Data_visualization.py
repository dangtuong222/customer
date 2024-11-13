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
    plt.figure(figsize=(7, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố độ tuổi')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()

def do_thi_luot_mua_hang():
    data_ct = Read.read()
    # Tính tổng số lần mua hàng của khách hàng
    data_ct['Total_Purchases'] = data_ct['NumDealsPurchases' ] + data_ct['NumWebPurchases'] + data_ct['NumCatalogPurchases'] + data_ct['NumStorePurchases']
    # Đảm bảo không có giá trị NaN trong cột Total_Purchases
    data_ct['Total_Purchases'] = pd.to_numeric(data_ct['Total_Purchases'], errors='coerce')
    # SẮP XẾP DỮ LIỆU
    sorted_data = np.sort(data_ct['Total_Purchases'])

    # TÍNH TOÁN CDF
    #Tạo một mảng y với các giá trị từ 1 đến số lượng phần tử trong sorted_data, 
    #sau đó chia cho tổng số phần tử để tính tỷ lệ tích lũy. Mảng y này thể hiện tỷ lệ phần trăm dữ liệu dưới mỗi giá trị trong sorted_data.
    y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

    # TẠO ĐỒ THỊ CDF    
    plt.figure(figsize=(8, 6))
    plt.step(sorted_data, y, color="red", linestyle='--', linewidth=1)

    # TÙY CHỈNH CỘT X,Y
    plt.xticks(np.arange(0,50, step=5))
    plt.yticks(np.arange(0, 1.1, 0.1))

    # GẮN NHÃN
    plt.xlabel('Tổng số mua hàng')
    plt.ylabel('Phân phối tích lũy')

    # ÁP DỤNG BG
    plt.style.use('ggplot')

    plt.show()

def bieu_do_phan_tich_hinh_thuc_mua_hang():
    data_ct = Read.read()
    
    # Chọn các cột chứa cả 'Num' và 'Purchases' trong tên cột
    purchase_columns = [col for col in data_ct.columns if 'Num' in col and 'Purchases' in col]
    purchase_df = data_ct[purchase_columns]

    # Làm phẳng DataFrame thành danh sách và tạo DataFrame mới với tên phương thức mua lặp lại
    total_purchases = purchase_df.values.flatten()
    purchase_names = ['Deal', 'Web', 'Catalog', 'Store'] * (len(total_purchases) // 4)

    # Tạo DataFrame cho Phương thức mua và Tổng lượt mua
    combined_df = pd.DataFrame({
        'Phương thức mua': purchase_names,
        'Tổng lượt mua': total_purchases
    })
    
    # Tạo biểu đồ boxplot
    sns.boxplot(data=combined_df, 
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
    data_ct = Read.read()
    
    # Plotting histogram
    plt.hist(data_ct['NumWebVisitsMonth'], weights=np.ones(len(data_ct['Total_Purchases'])) / len(data_ct['Total_Purchases'])*100, bins=5, alpha=0.5, color='pink', edgecolor='darkblue')

    # Customize the y-axis
    plt.gca().yaxis.set_major_formatter(PercentFormatter())

    # Determine the lower value of Total_Purchases
    lower_limit = data_ct['NumWebVisitsMonth'].min()

    # Set x-axis limits and ticks
    #plt.xlim(lower_limit, 20)
    plt.xticks(range(lower_limit, 21, 1))
    # Labeling
    plt.xlabel('Số Lần Truy Cập Web')
    plt.ylabel('Phần trăm')
    plt.show()

def do_thi_phan_bo_thoi_gian_gan_bo():
    data_ct = Read.read()
    current_year = date.today().year
        # Tính năm đăng ký của khách hàng
    data_ct['Dt_Customer'] = pd.to_datetime(data_ct['Dt_Customer'], errors='coerce')
    data_ct['Enrollment_Year'] = data_ct['Dt_Customer'].dt.year
    data_ct['Seniority'] = current_year - data_ct['Enrollment_Year']
    # Đổi tên cột 'Seniority' thành 'Total_Years' trong DataFrame
    tham_nien = data_ct[['Seniority']].rename(columns={'Seniority': 'Tổng Năm'})

    # Nhóm theo 'Tổng Năm' và tính số lượng mỗi nhóm
    tham_nien = tham_nien.groupby('Tổng Năm').size().reset_index(name='Số Lượng')

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    tham_nien['Phần Trăm'] = (tham_nien['Số Lượng'] * 100 / tham_nien['Số Lượng'].sum()).round(2)

    # Chuyển đổi 'Tổng Năm' thành biến phân loại (categorical)
    tham_nien['Tổng Năm'] = tham_nien['Tổng Năm'].astype('category')

    # Data
    labels = tham_nien['Tổng Năm']
    sizes = tham_nien['Phần Trăm']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]

    # Create a pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bổ thời gian gắn bó')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()

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
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố chi tiêu các năm')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()

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
    offers['Offers_Total'] = offers['Offers_Total'].astype('category')
    
    sns.set(style="whitegrid")  # Thiết lập phong cách đồ thị là lưới trắng
    # Tạo biểu đồ cột sử dụng seaborn
    sns.barplot(x='Offers_Total', y='num', data=offers, palette="Set2")

    # Thêm nhãn văn bản với phần trăm
    for index, row in offers.iterrows():
        plt.text(index, row['num'], f"{row['num']} ({row['percentage']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và tỷ lệ
    plt.xlabel('Tổng số ưu đãi')
    plt.ylabel('Số lượng')

    # Hiển thị biểu đồ
    plt.show()

def chien_dich_uu_dai():
    data_ct = Read.read()
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
    
    # Nhóm dữ liệu khách hàng theo 'Total_Offers' và tính giá trị trung vị của 'Income'
    result_df = data_ct.groupby('Total_Offers').agg(avg_spend=('Income', 'median')).reset_index().round(0)
    result_df.columns = ['Tổng Số Ưu Đãi', 'Chi Tiêu TB']
    
    # Thiết lập phong cách biểu đồ
    sns.set(style="whitegrid")

    # Tạo biểu đồ thanh sử dụng seaborn
    sns.barplot(x='Chiến dịch', y='Số Lượng', data=df_nhom)

    # Thêm nhãn văn bản với phần trăm
    for index, row in df_nhom.iterrows():
        plt.text(index, row['Số Lượng'], f"{row['Số Lượng']} ({row['Phần Trăm']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và thang đo
    plt.xlabel('Chiến dịch')
    plt.ylabel('Số Lượng')
    # Hiển thị biểu đồ
    plt.show()

def so_luong_trung_binh_cua_moi_san_pham():
    data_ct = Read.read()
    # Chọn các cột sản phẩm liên quan
    product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    # Tính trung bình cho mỗi loại sản phẩm
    average_quantities = data_ct[product_columns].mean()

    # Thiết lập kích thước và vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    average_quantities.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Average Quantity of Each Product Type")
    plt.xlabel("Product Type")
    plt.ylabel("Average Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()  # Tự động điều chỉnh bố cục để biểu đồ không bị cắt
    plt.show()

def so_sanh_thu_nhap_va_chi_tieu_50_khach_dau_tien():
    data_ct = Read.read()
    # Chọn các cột sản phẩm liên quan
    product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    # Tính tổng chi tiêu của mỗi khách hàng qua các loại sản phẩm
    data_ct['Total_Expenditure'] = data_ct[product_columns].sum(axis=1)
    # Loại bỏ các hàng thiếu dữ liệu thu nhập
    data_ct = data_ct.dropna(subset=['Income'])
    # Đảm bảo cột Income là kiểu float
    data_ct['Income'] = data_ct['Income'].astype(float)

    # Lấy mẫu dữ liệu 50 khách hàng đầu tiên
    sample_data = data_ct.head(50)

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

def bieu_do_phan_tich_muc_do_phan_nan():
    data_ct = Read.read()
    
    # Tạo nhóm độ tuổi
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    #Danh sách tên gọi của các nhóm tuổi tương ứng với các ngưỡng trong bins
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    #Sử dụng hàm cut để phân loại cột age trong tập dữ liệu đã làm sạch 
    #Tạo cột mới là nhóm tuổi dựa trên cột age 
    data_ct['AgeGroup'] = pd.cut(data_ct['Age'], bins=bins, labels=labels)
    # Tính số lượng phàn nàn trong từng nhóm tuổi
    grouped_data = data_ct.groupby(['AgeGroup', 'Complain'], observed=True).size().unstack(fill_value=0)
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

def bieu_do_tan_suat_mua_hang_theo_do_tuoi():
    data_ct = Read.read()
    
    # Tính tuổi của khách hàng từ năm sinh cho đến năm hiện tại
    current_year = pd.Timestamp.now().year
    # tạo cột mới tính tuổi bằng cách lấy năm hiện tại trừ đi cột year birth của từng khách hàng
    data_ct['Age'] = current_year - data_ct['Year_Birth']
    
    # Phân loại nhóm tuổi bằng cách tạo ra cột mới là AgeGroup
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
    labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
    #Chia dữ liệu trong cột Age thành các khoảng giá trị (hoặc nhóm) dựa trên các giá trị trong bins và gán nhãn cho #từng nhóm theo danh sách labels.
    data_ct['AgeGroup'] = pd.cut(data_ct['Age'], bins=bins, labels=labels)

    # Tính tổng tần suất mua hàng theo nhóm tuổi
    tan_suat_tuoi = data_ct.groupby('AgeGroup')[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum()

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