import Data_cleaning as Data_cleaning
import Read as Read
from tkinter import messagebox
def update_row_by_id(id, new_values):
    # Read the CSV file
    df = Read.read()
    
    # Check if 'ID' column exists
    if 'ID' not in df.columns:
        raise ValueError("Cột 'ID' không tồn tại trong DataFrame.")
    
    # Find the row with the given ID
    row_to_update = df[df['ID'] == id]
    
    if row_to_update.empty:
        raise ValueError(f"Không tìm thấy bản ghi có ID '{id}'.")
    
    # Get the index of the row to update
    index_to_update = row_to_update.index[0]
    
    # Get the columns of the DataFrame
    columns = df.columns
    
    # Check if the number of new values matches the number of columns
    if len(new_values) != len(columns):
        raise ValueError(f"Số lượng cột của giá trị mới({len(new_values)}) không trùng khớp với số cột của dataFrame({len(columns)})")
    
    # Update the row
    for col, value in zip(columns, new_values):
        df.at[index_to_update, col] = value
    
    # Reapply the cleaning and updating functions to ensure data consistency
    Data_cleaning.remove_null(df)
    Data_cleaning.update_Education(df)
    Data_cleaning.update_Marital_status(df)
    Data_cleaning.updateFrame(df)
    
    # Save the updated DataFrame
    Read.save_file(df)
    
    messagebox.showinfo("Thành công", f"Bản ghi có ID '{id}' đã được cập nhật thành công.")
    return df