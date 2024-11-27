import Data_cleaning as Data_cleaning
import CRUD.Read as Read
from tkinter import messagebox

def update_row_by_id(id, new_values):
    try:
        # Đọc dữ liệu từ file
        df = Read.read()

        # Kiểm tra cột 'ID' có tồn tại
        if 'ID' not in df.columns:
            messagebox.showerror("Lỗi", "Cột 'ID' không tồn tại trong DataFrame.")
            return None

        # Kiểm tra xem ID có tồn tại không
        if str(id) not in df['ID'].astype(str).values:
            messagebox.showerror("Lỗi", f"Không tìm thấy bản ghi có ID '{id}'.")
            return None

        # Kiểm tra số lượng giá trị mới có khớp với số lượng cột
        if len(new_values) != len(df.columns):
            messagebox.showerror(
                "Lỗi", 
                f"Số lượng giá trị mới không khớp với số lượng cột (cần {len(df.columns)}, nhận {len(new_values)})."
            )
            return None

        # Kiểm tra giá trị trống trong new_values
        if any(value == "" for value in new_values):
            messagebox.showerror("Lỗi", "Danh sách giá trị mới có chứa giá trị trống.")
            return None

        # Xác định chỉ mục của hàng cần cập nhật
        index_to_update = df[df['ID'].astype(str) == str(id)].index[0]

        # Cập nhật giá trị mới
        df.loc[index_to_update] = new_values

        # Áp dụng các bước làm sạch dữ liệu
        Data_cleaning.update_Education(df)
        Data_cleaning.update_Marital_status(df)

        # Lưu DataFrame sau khi cập nhật
        Read.save_file(df)

        messagebox.showinfo("Thành công", f"Bản ghi có ID '{id}' đã được cập nhật thành công.")
        return df

    except Exception as e:
        # Bắt lỗi và hiển thị thông báo
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        return None
