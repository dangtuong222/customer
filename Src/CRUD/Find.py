import CRUD.Read as Read

def find_by_id(id):
    # Read the data
    df = Read.read()
    
    # Check if 'ID' column exists
    if 'ID' not in df.columns:
        raise ValueError("Cột 'ID' không tồn tại trong DataFrame.")
    
    # Find the row with the given ID
    result = df[df['ID'] == id]
    
    if result.empty:
        return None
    else:
        return result.iloc[0]

def display_record(record):
    if record is None:
        print("Không tìm thấy bản ghi với ID đã cho.")
    else:
        for column, value in record.items():
            print(f"{column}: {value}")