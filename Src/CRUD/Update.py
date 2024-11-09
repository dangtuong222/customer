import Data_cleaning as Data_cleaning
import CRUD.Read as Read

def update_row_by_index(index, new_values):
    # Read the CSV file
    df = Read.read()
    
    # Check if the index exists in the DataFrame
    if index not in df.index:
        raise ValueError(f"Bản ghi thứ {index} không tồn tại.")
    
    # Get the columns of the DataFrame
    columns = df.columns
    
    # Check if the number of new values matches the number of columns
    if len(new_values) != len(columns):
        raise ValueError(f"Số lượng cột của giá trị mới({len(new_values)}) không trùng khớp với số cột của dataFrame({len(columns)})")
    
    # Update the row
    for col, value in zip(columns, new_values):
        df.at[index, col] = value
    
    # Reapply the cleaning and updating functions to ensure data consistency
    Data_cleaning.remove_null(df)
    Data_cleaning.update_Education(df)
    Data_cleaning.update_Marital_status(df)
    Data_cleaning.updateFrame(df)
    
    # Save the updated DataFrame
    Read.save_file(df)
    
    print(f"Bản ghi số {index} đã được cập nhật thành công.")
    return df

# Example usage
# if __name__ == "__main__":
#     try:
#         # Example: Update row at index 0 with new values
#         new_values = [1955, "Master", "Single", 60000, "2013-01-01", 30, 100, 5, 70, 3, 2, 25, 4, 4, 2, 5, 6, 1, 1, 1, 1, 1, 0, 69]
#         updated_df = update_row_by_index(0, new_values)
        
#         # Display the updated row
#         print("\nUpdated row:")
#         print(updated_df.loc[0])
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")