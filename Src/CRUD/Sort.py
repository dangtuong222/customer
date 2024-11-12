import CRUD.Read as Read

def sort_by_income(ascending=True):
    # Đọc dữ liệu
    df = Read.read()
    
    # Kiểm tra xem cột 'Income' có tồn tại không
    if 'Income' not in df.columns:
        raise ValueError("Cột 'Income' không tồn tại trong DataFrame.")
    
    # Sắp xếp DataFrame theo cột 'Income'
    df_sorted = df.sort_values(by='Income', ascending=ascending)
    
    # Reset index sau khi sắp xếp
    df_sorted = df_sorted.reset_index(drop=True)
    
    return df_sorted

def display_sorted_data(df, num_rows=10):
    # Hiển thị một số hàng đầu tiên của DataFrame đã sắp xếp
    print(df.head(num_rows).to_string(index=False))

# Tăng dần -> truyền tham số bằng TRUE
# Giảm dần -> truyền tham số bằng FALSE