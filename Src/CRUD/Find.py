import CRUD.Read as Read
from tkinter import messagebox
def find_by_id(id):
    # Read the data
    df = Read.read()
    
    # Check if 'ID' column exists
    if 'ID' not in df.columns:
        messagebox.showerror("Lỗi", "Cột 'ID' không tồn tại trong DataFrame.")
    
    # Find the row with the given ID
    result = df[df['ID'] == id]
    
    if result.empty:
        return None, messagebox.showerror("Lỗi", "Không tìm thấy ID!")
    else:
        return result.iloc[0]
