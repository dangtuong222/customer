from ast import Delete
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import CRUD.Create as Create
import Data_visualization
import CRUD.Read as Read
import CRUD.Update as Update

# class MarketingCampaignUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Marketing Campaign Analysis")
#         self.master.geometry("1000x600")

#         # Create notebook (tabbed interface)
#         self.notebook = ttk.Notebook(self.master)
#         self.notebook.pack(expand=True, fill='both')

#         # Create tabs
#         self.view_tab = ttk.Frame(self.notebook)
#         self.create_tab = ttk.Frame(self.notebook)
#         self.update_tab = ttk.Frame(self.notebook)
#         self.delete_tab = ttk.Frame(self.notebook)
#         self.visualize_tab = ttk.Frame(self.notebook)

#         self.notebook.add(self.view_tab, text='View Data')
#         self.notebook.add(self.create_tab, text='Create Record')
#         self.notebook.add(self.update_tab, text='Update Record')
#         self.notebook.add(self.delete_tab, text='Delete Record')
#         self.notebook.add(self.visualize_tab, text='Visualize Data')

#         self.setup_view_tab()
#         self.setup_create_tab()
#         self.setup_update_tab()
#         self.setup_delete_tab()
#         self.setup_visualize_tab()

#     def setup_view_tab(self):
#         # Create Treeview
#         self.tree = ttk.Treeview(self.view_tab)
#         self.tree.pack(expand=True, fill='both')

#         # Add a scrollbar
#         scrollbar = ttk.Scrollbar(self.view_tab, orient="vertical", command=self.tree.yview)
#         scrollbar.pack(side='right', fill='y')
#         self.tree.configure(yscrollcommand=scrollbar.set)

#         # Load data button
#         load_button = ttk.Button(self.view_tab, text="Load Data", command=self.load_data)
#         load_button.pack(pady=10)

#     def load_data(self):
#         df = Read.read()
        
#         # Clear existing data
#         self.tree.delete(*self.tree.get_children())
        
#         # Set up columns
#         self.tree["columns"] = list(df.columns)
#         for col in df.columns:
#             self.tree.heading(col, text=col)
#             self.tree.column(col, width=100)

#         # Insert data
#         for i, row in df.iterrows():
#             self.tree.insert("", "end", values=list(row))

#     def setup_create_tab(self):
#         # Create form fields
#         fields = ['Year_Birth', 'Education', 'Marital_Status', 'Income', 'Dt_Customer', 'Recency', 'MntWines',
#                   'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 
#                   'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 
#                   'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 
#                   'AcceptedCmp2', 'Complain', 'Response']
        
#         self.create_entries = {}
#         for i, field in enumerate(fields):
#             label = ttk.Label(self.create_tab, text=field)
#             label.grid(row=i, column=0, padx=5, pady=2)
#             entry = ttk.Entry(self.create_tab)
#             entry.grid(row=i, column=1, padx=5, pady=2)
#             self.create_entries[field] = entry

#         create_button = ttk.Button(self.create_tab, text="Create Record", command=self.create_record)
#         create_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

#     def create_record(self):
#         # Get values from entries
#         values = {field: entry.get() for field, entry in self.create_entries.items()}
#         try:
#             Create.Create(**values)
#             messagebox.showinfo("Success", "Record created successfully!")
#             self.load_data()  # Refresh the view
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def setup_update_tab(self):
#         ttk.Label(self.update_tab, text="Index to update:").pack(pady=5)
#         self.update_index_entry = ttk.Entry(self.update_tab)
#         self.update_index_entry.pack(pady=5)

#         ttk.Label(self.update_tab, text="New values (comma-separated):").pack(pady=5)
#         self.update_values_entry = ttk.Entry(self.update_tab)
#         self.update_values_entry.pack(pady=5)

#         update_button = ttk.Button(self.update_tab, text="Update Record", command=self.update_record)
#         update_button.pack(pady=10)

#     def update_record(self):
#         try:
#             index = int(self.update_index_entry.get())
#             new_values = self.update_values_entry.get().split(',')
#             Update.update_row_by_index(index, new_values)
#             messagebox.showinfo("Success", f"Record at index {index} updated successfully!")
#             self.load_data()  # Refresh the view
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def setup_delete_tab(self):
#         ttk.Label(self.delete_tab, text="Index to delete:").pack(pady=5)
#         self.delete_index_entry = ttk.Entry(self.delete_tab)
#         self.delete_index_entry.pack(pady=5)

#         delete_button = ttk.Button(self.delete_tab, text="Delete Record", command=self.delete_record)
#         delete_button.pack(pady=10)

#     def delete_record(self):
#         try:
#             index = int(self.delete_index_entry.get())
#             Delete.Delete_by_index(index)
#             self.load_data()  # Refresh the view
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def setup_visualize_tab(self):
#         visualizations = [
#             ("Age Distribution", Data_visualization.do_thi_phan_bo_do_tuoi),
#             ("Purchase Distribution", Data_visualization.do_thi_luot_mua_hang),
#             ("Purchase Methods", Data_visualization.bieu_do_phan_tich_hinh_thuc_mua_hang),
#             ("Web Visits", Data_visualization.do_thi_so_luot_truy_cap_web),
#             ("Customer Loyalty", Data_visualization.do_thi_phan_bo_thoi_gian_gan_bo),
#             ("Yearly Expenditure", Data_visualization.do_thi_tong_chi_tieu_cac_nam),
#             ("Campaign Performance", Data_visualization.hieu_suat_chien_dich),
#             ("Campaign Offers", Data_visualization.chien_dich_uu_dai),
#             ("Average Product Quantity", Data_visualization.so_luong_trung_binh_cua_moi_san_pham),
#             ("Income vs Expenditure", Data_visualization.so_sanh_thu_nhap_va_chi_tieu_50_khach_dau_tien),
#             ("Complaints by Age", Data_visualization.bieu_do_phan_tich_muc_do_phan_nan),
#             ("Purchase Frequency by Age", Data_visualization.bieu_do_tan_suat_mua_hang_theo_do_tuoi)
#         ]

#         for i, (text, func) in enumerate(visualizations):
#             button = ttk.Button(self.visualize_tab, text=text, command=lambda f=func: self.show_visualization(f))
#             button.grid(row=i//3, column=i%3, padx=5, pady=5)

#     def show_visualization(self, vis_func):
#         # Clear previous plot
#         for widget in self.visualize_tab.winfo_children():
#             if isinstance(widget, FigureCanvasTkAgg):
#                 widget.get_tk_widget().destroy()

#         # Create new plot
#         fig = plt.figure(figsize=(10, 6))
#         vis_func()
        
#         # Embed the plot
#         canvas = FigureCanvasTkAgg(fig, master=self.visualize_tab)
#         canvas.draw()
#         canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# def main():
#     root = tk.Tk()
#     app = MarketingCampaignUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()