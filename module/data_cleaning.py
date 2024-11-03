from datetime import date
import pandas as pd
import CRUD


# xoa cac gia tri con thieu(null)
CRUD.df.dropna(inplace= True)

CRUD.custom_df['Education'] = CRUD.custom_df['Education'].apply(lambda i: 'Master' if i == '2n Cycle' else i)
# thay hàng có dữ liệu '2n Cycle' thành 'Master'


# Ở cột Marital_Status chỉ giữ lại 2 giá trị là 'Single' và 'In relationship'
CRUD.custom_df['Marital_Status'] = CRUD.custom_df['Marital_Status'].apply(lambda i: 'in relationship' if i == 'Together' or i == 'Married' else i)
# thay hàng có dữ liệu 'Togethe' và 'Married' thành 'In relationship'
CRUD.custom_df['Marital_Status'] = CRUD.custom_df['Marital_Status'].apply(lambda i: 'Single' if i != 'Single' and i != 'in relationship' else i)
# thay tất cả các giá trị còn lại thành 'Single'


