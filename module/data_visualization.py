import data_connection
import data_cleaning
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter
from scipy import stats

def do_thi_phan_bo_do_tuoi():
    
    # Tính phần trăm độ tuổi
    age_range = data_cleaning.custom_df.groupby('Age_Group').size().reset_index(name='num')
    age_range['percentage'] = (age_range['num'] * 100 / age_range['num'].sum()).round(2)
    print(age_range)

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
    
def do_thi_CDF_tong_so_mua_hang():
    
    # SẮP XẾP DỮ LIỆU
    sorted_data = np.sort(data_cleaning.custom_df['Total_Purchases'])

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
    
def do_thi_luot_mua_hang():
    
    # SẮP XẾP DỮ LIỆU
    sorted_data = np.sort(data_cleaning.custom_df['Total_Purchases'])

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
    
    # Giả sử bạn có DataFrame tên là custom_df
    # Chọn các cột chứa cả 'Num' và 'Purchases' trong tên cột
    purchase_columns = [col for col in data_cleaning.custom_df.columns if 'Num' in col and 'Purchases' in col]
    purchase_df = data_cleaning.custom_df[purchase_columns]

    # Làm phẳng DataFrame thành danh sách và tạo DataFrame mới với tên phương thức mua lặp lại
    total_purchases = purchase_df.values.flatten()
    purchase_names = ['Deal', 'Web', 'Catalog', 'Store'] * (len(total_purchases) // 4)

    # Tạo DataFrame cho Phương thức mua và Tổng lượt mua
    combined_df = pd.DataFrame({
        'Phương thức mua': purchase_names,
        'Tổng lượt mua': total_purchases
    })

    # Hiển thị 4 hàng đầu tiên của DataFrame kết quả
    print(combined_df.head(4))
    
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
    
    
    # Giả sử bạn có một DataFrame tên là combined_df
    # Nhóm theo 'Phương thức mua' và tính tổng 'Tổng lượt mua' cho mỗi nhóm
    grouped_df = combined_df.groupby('Phương thức mua')['Tổng lượt mua'].sum().reset_index()

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    grouped_df['Phần trăm'] = (grouped_df['Tổng lượt mua'] * 100 / grouped_df['Tổng lượt mua'].sum()).round(2)

    # Hiển thị DataFrame kết quả
    print(grouped_df)
    # -------------------------- 

def do_thi_so_luot_truy_cap_web():
    
    # 
    # Plotting histogram
    plt.hist(data_cleaning.custom_df['NumWebVisitsMonth'], weights=np.ones(len(data_cleaning.custom_df['Total_Purchases'])) / len(data_cleaning.custom_df['Total_Purchases'])*100, bins=5, alpha=0.5, color='pink', edgecolor='darkblue')

    # Customize the y-axis
    plt.gca().yaxis.set_major_formatter(PercentFormatter())

    # Determine the lower value of Total_Purchases
    lower_limit = data_cleaning.custom_df['NumWebVisitsMonth'].min()

    # Set x-axis limits and ticks
    #plt.xlim(lower_limit, 20)
    plt.xticks(range(lower_limit, 21, 1))


    # Labeling
    plt.xlabel('Số Lần Truy Cập Web')
    plt.ylabel('Phần trăm')

    plt.show()
    
def do_thi_CDF_truy_cap_web():
    
    # Sắp xếp
    sorted_purchases = np.sort(data_cleaning.custom_df['NumWebVisitsMonth'])

    # Tính CDF
    y = np.arange(1, len(sorted_purchases) + 1) / len(sorted_purchases)

    # Tạo biểu đồ CDF
    plt.figure(figsize=(8, 6))
    plt.step(sorted_purchases, y, color="#00AFBB", linestyle='--', linewidth=1)

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
    # Đổi tên cột 'Seniority' thành 'Total_Years' trong DataFrame
    tham_nien = data_cleaning.custom_df[['Seniority']].rename(columns={'Seniority': 'Tổng Năm'})

    # Nhóm theo 'Tổng Năm' và tính số lượng mỗi nhóm
    tham_nien = tham_nien.groupby('Tổng Năm').size().reset_index(name='số_lượng')

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    tham_nien['phần_trăm'] = (tham_nien['số_lượng'] * 100 / tham_nien['số_lượng'].sum()).round(2)

    # Chuyển đổi 'Tổng Năm' thành biến phân loại (categorical)
    tham_nien['Tổng Năm'] = tham_nien['Tổng Năm'].astype('category')
    
    # Hiển thị kết quả:
    print(tham_nien)

    sns.set(style="whitegrid")  # Thiết lập phong cách đồ thị là lưới trắng

    # Tạo biểu đồ cột sử dụng seaborn
    sns.barplot(x='Tổng Năm', y='số_lượng', data=tham_nien, palette=["#41B7C4", "#CCEDB1", "#F5CA63"])

    # Thêm nhãn văn bản với phần trăm   
    for index, row in tham_nien.iterrows():
        plt.text(index, row['số_lượng'], f"{row['số_lượng']} ({row['phần_trăm']}%)", va='bottom', ha='center')

    # Tùy chỉnh nhãn và tỷ lệ
    plt.xlabel('Số Năm')
    plt.ylabel('Số Lượng')

    # Hiển thị biểu đồ
    plt.show()
    
def do_thi_phan_bo_thoi_gian_gan_bo():
    # Đổi tên cột 'Seniority' thành 'Total_Years' trong DataFrame
    tham_nien = data_cleaning.custom_df[['Seniority']].rename(columns={'Seniority': 'Tổng Năm'})

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
    # Giả sử custom_df đã được định nghĩa
    
    # Nhóm theo 'Enrollment_Year' và tính tổng 'Total_Spent' cho mỗi nhóm
    grouped_df = data_cleaning.custom_df.groupby('Enrollment_Year')['Total_Spent'].sum().reset_index()

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    grouped_df['percentage'] = (grouped_df['Total_Spent'] * 100 / grouped_df['Total_Spent'].sum()).round(2)

    # Đổi tên các cột sang tiếng Việt để in kết quả
    grouped_df.columns = ['Năm Đăng Ký', 'Tổng Chi Tiêu', 'Phần Trăm']

    # Hiển thị kết quả
    print(grouped_df)
    
    labels = grouped_df['Năm Đăng Ký']
    sizes = grouped_df['Phần Trăm']
    colors = ["#41B7C4", "#CCEDB1", "#F5CA63", "#808A87"]
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.title('Phân bố chi tiêu các năm')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    plt.show()
    
def tuong_quan_giua_thu_nhap_va_so_lan_mua_hang():
    # Thực hiện kiểm tra tương quan
    correlation_coefficient, p_value = stats.pearsonr(data_cleaning.custom_df['Income'], data_cleaning.custom_df['Total_Purchases'])

    # Print the results
    print("Hệ số tương quan:", correlation_coefficient)
    print("Giá trị P:", p_value)
    
    sns.set(style="whitegrid")

    # Create the scatterplot
    sns.scatterplot(data=data_cleaning.custom_df, x="Income", y="Total_Purchases", color="green", edgecolor="black", linewidth=0.5, s=40)

    # Set x-axis limits and ticks
    plt.xlim(0, 200000)
    plt.xticks(range(0, 200001, 20000))

    # Set y-axis limits and ticks
    #plt.ylim(0, 4000)
    #plt.yticks(range(0, 4001, 1000))

    # Add a linear regression line
    sns.regplot(data=data_cleaning.custom_df, x="Income", y="Total_Purchases", scatter=False, color="darkred", line_kws={"linestyle": "--"})
    plt.xlabel('Thu Nhập')
    plt.ylabel('Tổng Số Mua')
    # Display the plot
    plt.show()
    
def hieu_suat_chien_dich():
    # Đổi tên cột 'Total_Offers' thành 'Offers_Total'
    offers = data_cleaning.custom_df[['Total_Offers']].rename(columns={'Total_Offers': 'Offers_Total'})

    # Nhóm theo 'Offers_Total' và tính số lượng mỗi nhóm
    offers = offers.groupby('Offers_Total').size().reset_index(name='num')

    # Tính phần trăm và làm tròn đến 2 chữ số thập phân
    # Chú ý: nên sử dụng tổng của cột 'num' trong DataFrame 'offers' chứ không phải 'seniority'
    offers['percentage'] = (offers['num'] * 100 / offers['num'].sum()).round(2)

    # Chuyển đổi 'Offers_Total' thành biến phân loại (categorical)
    offers['Offers_Total'] = offers['Offers_Total'].astype('category')

    # Hiển thị DataFrame kết quả
    print(offers)
    
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
    # Giả sử custom_df đã được định nghĩa
    cmp_df = data_cleaning.custom_df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']]
    # Kiểm tra số lượng khách hàng
    num_customers = cmp_df.shape[0]
    # Tạo cột Campaign
    Campaign = pd.DataFrame({'Chiến dịch': ['Chiến dịch 1', 'Chiến dịch 2', 'Chiến dịch 3', 'Chiến dịch 4', 'Chiến dịch 5'] * num_customers})
    # Tạo cột No_Of_Offers
    No_Of_Offers = pd.DataFrame({'Số lượt ưu đãi': cmp_df.values.flatten()})
    # Kết hợp Campaign và No_Of_Offers vào cmp_df
    cmp_df = pd.concat([Campaign, No_Of_Offers], axis=1)
    # Hiển thị 3 hàng đầu tiên
    print(cmp_df.head(5))
    print("\n")
    
    # Lọc các hàng mà Số Lượng Ưu Đãi bằng 1
    df_loc = cmp_df[cmp_df['Số lượt ưu đãi'] == 1]
    # Nhóm theo Chiến Dịch và tính số lượng hàng trong mỗi nhóm
    df_nhom = df_loc.groupby('Chiến dịch').size().reset_index(name='Số Lượng')
    # Tính phần trăm
    df_nhom['Phần Trăm'] = (df_nhom['Số Lượng'] * 100 / df_nhom['Số Lượng'].sum()).round(2)
    # Hiển thị kết quả
    print(df_nhom)
    print("\n")
    
    # Nhóm dữ liệu khách hàng theo 'Total_Offers' và tính giá trị trung vị của 'Income'
    result_df = data_cleaning.custom_df.groupby('Total_Offers').agg(avg_spend=('Income', 'median')).reset_index().round(0)
    result_df.columns = ['Tổng Số Ưu Đãi', 'Chi Tiêu TB']
    print(result_df)
    
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
    
    
