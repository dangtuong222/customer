import data_cleaning

class Marketing_campaign():
    def __init__(self, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response):
        self.Year_Birth = Year_Birth
        self.Education = Education
        self.Marital_Status = Marital_Status
        self.Income = Income
        self.Kidhome = Kidhome
        self.Teenhome = Teenhome
        self.Dt_Customer = Dt_Customer
        self.Recency = Recency
        self.MntWines = MntWines
        self.MntFruits = MntFruits
        self.MntMeatProducts = MntMeatProducts
        self.MntFishProducts = MntFishProducts
        self.MntSweetProducts = MntSweetProducts
        self.MntGoldProds = MntGoldProds
        self.NumDealsPurchases = NumDealsPurchases
        self.NumWebPurchases = NumWebPurchases
        self.NumCatalogPurchases = NumCatalogPurchases
        self.NumStorePurchases = NumStorePurchases
        self.NumWebVisitsMonth = NumWebVisitsMonth
        self.AcceptedCmp3 = AcceptedCmp3
        self.AcceptedCmp4 = AcceptedCmp4
        self.AcceptedCmp5 = AcceptedCmp5
        self.AcceptedCmp1 = AcceptedCmp1
        self.AcceptedCmp2 = AcceptedCmp2
        self.Complain = Complain
        self.Response = Response
        
    def Create(self, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response):
        new_row = {"Year_Birth": Year_Birth, 
                   "Education": Education, 
                   "Marital_Status": Marital_Status,
                   "Income": Income,
                   "Kidhome": Kidhome,
                   "Teenhome": Teenhome,
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
        data_cleaning.custom_df.loc[len(data_cleaning.custom_df)] = new_row
        
    def Read():
        print(data_cleaning.custom_df.to_string())