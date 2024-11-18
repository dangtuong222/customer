import CRUD.Read as Read
import pandas as pd
import Data_cleaning as Data_cleaning
from tkinter import messagebox

def Create(ID, Year_Birth, Education, Marital_Status, Income, Dt_Customer, Recency, MntWines,
           MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases,
           NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3,
           AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response):
    # Đọc dữ liệu từ hàm Read.read()
    df = Read.read()
    try:
        # Kiểm tra cột 'ID' có tồn tại hay không
        if 'ID' not in df.columns:
            messagebox.showerror("Lỗi", "Cột 'ID' không tồn tại trong DataFrame.")
            return None

        # Tạo bản ghi mới dưới dạng dictionary
        new_row = {
            "ID": ID,
            "Year_Birth": Year_Birth,
            "Education": Education,
            "Marital_Status": Marital_Status,
            "Income": Income,
            "Dt_Customer": Dt_Customer,
            "Recency": Recency,
            "MntWines": MntWines,
            "MntFruits": MntFruits,
            "MntMeatProducts": MntMeatProducts,
            "MntFishProducts": MntFishProducts,
            "MntSweetProducts": MntSweetProducts,
            "MntGoldProds": MntGoldProds,
            "NumDealsPurchases": NumDealsPurchases,
            "NumWebPurchases": NumWebPurchases,
            "NumCatalogPurchases": NumCatalogPurchases,
            "NumStorePurchases": NumStorePurchases,
            "NumWebVisitsMonth": NumWebVisitsMonth,
            "AcceptedCmp3": AcceptedCmp3,
            "AcceptedCmp4": AcceptedCmp4,
            "AcceptedCmp5": AcceptedCmp5,
            "AcceptedCmp1": AcceptedCmp1,
            "AcceptedCmp2": AcceptedCmp2,
            "Complain": Complain,
            "Response": Response
        }
        # Đồng nhất kiểu dữ liệu của cột 'ID' và giá trị ID
        df['ID'] = df['ID'].astype(str)
        ID = str(ID)

        # Kiểm tra xem ID đã tồn tại hay chưa
        if ID in df['ID'].values:
            messagebox.showerror("Lỗi", "ID đã tồn tại.")
            return None
            
        # Tạo DataFrame mới từ bản ghi mới
        new_record_df = pd.DataFrame([new_row])

        # Đảm bảo cột của bản ghi mới phù hợp với DataFrame hiện tại
        new_record_df = new_record_df.reindex(columns=df.columns)

        # Gộp bản ghi mới vào DataFrame hiện tại
        df = pd.concat([df, new_record_df], ignore_index=True)

        # Áp dụng các bước làm sạch dữ liệu
        Data_cleaning.remove_null(df)
        Data_cleaning.update_Education(df)
        Data_cleaning.update_Marital_status(df)
        df = Data_cleaning.delete_columm(df)

        # Lưu DataFrame đã cập nhật
        Read.save_file(df)
        messagebox.showinfo("Thành công", "Bản ghi đã được thêm thành công!")
        return df
            
    except Exception as e:
        # Hiển thị lỗi nếu có lỗi xảy ra
        messagebox.showerror("Lỗi", e)
        return None
