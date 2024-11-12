from CRUD.Create import Create
from CRUD.Delete import Delete_by_ID
from CRUD.Read import read
from CRUD.showdata import show_all_rows
from CRUD.Update import update_row_by_id
from CRUD.Sort import sort_by_income, display_sorted_data
from CRUD.Find import find_by_id, display_record
df = Create(2023, 2003, "Master", "Single", 232, "2012-04-02", 121, 32, 3, 3, 4, 4, 5, 3, 5, 3, 5, 3, 0, 0, 0, 0, 0, 0, 0)
print(df)

# display_record(find_by_id(8614))