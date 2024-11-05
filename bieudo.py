import datetime
import matplotlib.pyplot as plt  # type: ignore
import pandas as pd # type: ignore

# In ra phiên bản của pandas
print(pd.__version__)

# Đọc dữ liệu từ file Excel
file_path = r'D:\python\pjday1\marketing_campaign.xlsx'
data = pd.read_excel(file_path)

# Biểu đồ thứ 1: Biểu đồ thanh cho Số lượng trung bình của mỗi loại sản phẩm
# Chọn các cột sản phẩm liên quan
product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
# Tính trung bình cho mỗi loại sản phẩm
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

# Biểu đồ thứ 2: Biểu đồ phân phối độ tuổi của khách hàng
# Tạo cột Age dựa trên năm sinh của khách hàng
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

# Biểu đồ thứ 3: So sánh tổng thu nhập và tổng chi tiêu của 50 khách hàng đầu tiên
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

# Biểu đồ thứ 4: Biểu đồ phân phối số lượng lượt truy cập web mỗi tháng
# Lấy cột số lượt truy cập web
web_visits = data['NumWebVisitsMonth']

# Vẽ biểu đồ histogram cho phân phối lượt truy cập web
plt.figure(figsize=(10, 6))
plt.hist(web_visits, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Web Visits per Month')
plt.xlabel('Number of Web Visits in a Month')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Biểu đồ thứ 5: Biểu đồ thanh cho tổng số lượng mua hàng theo vị trí
# Tổng hợp số lượng mua hàng ở các vị trí khác nhau (web, catalog, cửa hàng)
purchase_locations = data[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum()

# Vẽ biểu đồ thanh cho các vị trí mua hàng
plt.figure(figsize=(10, 6))
purchase_locations.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'], edgecolor='black')
plt.title('Total Purchases by Location')
plt.xlabel('Purchase Location')
plt.ylabel('Total Number of Purchases')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
