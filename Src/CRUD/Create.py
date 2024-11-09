import CRUD.Read as Read
import pandas as pd
import Data_cleaning as Data_cleaning

def Create(Year_Birth, Education, Marital_Status, Income, Dt_Customer, Recency, MntWines,
           MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases,
           NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3,
           AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response):
    # Create the new row as a dictionary
    new_row = {
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
    Data_cleaning.remove_null(df)
    Data_cleaning.update_Education(df)
    Data_cleaning.update_Marital_status(df)
    Data_cleaning.delete_columm(df)
    Data_cleaning.updateFrame(df)
    new_record_df = pd.DataFrame([new_row])
    
    df = Read.read()
    df = pd.concat([df, new_record_df], ignore_index=True)
    
    Read.save_file(df)
    
    return df