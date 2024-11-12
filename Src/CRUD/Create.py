import CRUD.Read as Read
import pandas as pd
import Data_cleaning as Data_cleaning
from tkinter import messagebox

def Create(ID, Year_Birth, Education, Marital_Status, Income, Dt_Customer, Recency, MntWines,
           MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases,
           NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3,
           AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response):
    try:
        # Read the existing DataFrame
        df = Read.read()

        # Create the new row as a dictionary
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

        # Create a new DataFrame with the new row
        new_record_df = pd.DataFrame([new_row])

        # Ensure that the new record has the same columns as the existing DataFrame
        new_record_df = new_record_df.reindex(columns=df.columns)

        # Concatenate the new record with the existing DataFrame
        df = pd.concat([df, new_record_df], ignore_index=True)

        # Apply data cleaning operations
        Data_cleaning.remove_null(df)
        Data_cleaning.update_Education(df)
        Data_cleaning.update_Marital_status(df)
        Data_cleaning.delete_columm(df)
        Data_cleaning.updateFrame(df)

        # Save the updated DataFrame
        Read.save_file(df)

        return df, messagebox.showinfo("Thành công", "Bản ghi đã được thêm thành công!")

    except Exception as e:
        return None, messagebox.showerror("Lỗi", f"Thêm bản ghi thất bại.")