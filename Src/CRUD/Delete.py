import CRUD.Read as Read
from tkinter import messagebox
def Delete_by_ID(id):
    df = Read.read()
    if 'ID' in df.columns:
        row_to_delete = df[df['ID'] == id]
        if not row_to_delete.empty:
            df = df[df['ID'] != id]
            df.reset_index(drop=True, inplace=True)
            Read.save_file(df)
            messagebox.showinfo("Thành công", f"Bản ghi có ID '{id}' đã được xóa thành công!")
        else:
            messagebox.showerror("Lỗi", f"Không tìm thấy bản ghi có ID '{id}'.")
    else:
        messagebox.showerror("Lỗi", "Cột 'ID' không tồn tại trong DataFrame.")
    
    return df