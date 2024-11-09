import CRUD.Read as Read
from tkinter import messagebox
def Delete_by_index(index):
    df = Read.read()
    index_to_drop = index
    if index_to_drop in df.index:    
        df = df.drop(index_to_drop, axis=0)
        df = df.reset_index(drop=True, inplace=True)
        Read.save_file()
        messagebox.showinfo("Thành công", f"Bản ghi thứ '{index_to_drop}' đã được xóa thành công!")
    else:
        messagebox.showerror("Lỗi", f"Bản ghi '{index_to_drop}' không tồn tại.")
    
    return df