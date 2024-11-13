import Data_cleaning as Data_cleaning
import CRUD.Read as Read
from tkinter import messagebox
def update_row_by_id(id, new_values):
    # Read the CSV file
    df = Read.read()
    
    # Check if 'ID' column exists
    if 'ID' not in df.columns:
        messagebox.showerror("Lỗi", "Cột 'ID' không tồn tại trong DataFrame.")
    
    # Find the row with the given ID
    row_to_update = df[df['ID'] == id]
    
    if row_to_update.empty:
        messagebox.showerror("Lỗi", f"Không tìm thấy bản ghi có ID '{id}'.")
    
    # Get the index of the row to update
    index_to_update = row_to_update.index[0]
    
    # Get the columns of the DataFrame
    columns = df.columns
    
    # Update the row
    for col, value in zip(columns, new_values):
        df.at[index_to_update, col] = value
    
    # Reapply the cleaning and updating functions to ensure data consistency
    Data_cleaning.remove_null(df)
    Data_cleaning.update_Education(df)
    Data_cleaning.update_Marital_status(df)

    
    # Save the updated DataFrame
    Read.save_file(df)
    
    messagebox.showinfo("Thành công", f"Bản ghi có ID '{id}' đã được cập nhật thành công.")
    return df