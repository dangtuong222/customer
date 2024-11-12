import tkinter as tk
from tkinter import ttk, messagebox
from CRUD.Create import Create
from CRUD.Read import read
from CRUD.Delete import Delete_by_ID
from CRUD.Update import update_row_by_id
import Data_visualization as DataViz
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class MarketingCampaignApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Marketing Campaign Analysis")
        self.master.geometry("1200x800")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_crud_tab()
        self.create_visualization_tab()

    def create_crud_tab(self):
        crud_frame = ttk.Frame(self.notebook)
        self.notebook.add(crud_frame, text="CRUD Operations")

        # CRUD operation buttons
        button_frame = ttk.Frame(crud_frame)
        button_frame.pack(pady=10)

        operations = [("Create", self.show_create_panel),
                      ("Read", self.show_read_panel),
                      ("Update", self.show_update_panel),
                      ("Delete", self.show_delete_panel)]

        for text, command in operations:
            ttk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

        # Frame to hold operation panels
        self.operation_frame = ttk.Frame(crud_frame)
        self.operation_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Initialize panels
        self.create_panel()
        self.read_panel()
        self.update_panel()
        self.delete_panel()

        # Show Read panel by default
        self.show_read_panel()

    def create_panel(self):
        self.create_frame = ttk.Frame(self.operation_frame)
        
        create_attributes = ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                             "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                             "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                             "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                             "AcceptedCmp2", "Complain", "Response"]

        self.create_entries = {}
        for i, attr in enumerate(create_attributes):
            ttk.Label(self.create_frame, text=attr).grid(row=i, column=0, padx=5, pady=2, sticky="e")
            self.create_entries[attr] = ttk.Entry(self.create_frame)
            self.create_entries[attr].grid(row=i, column=1, padx=5, pady=2, sticky="w")

        ttk.Button(self.create_frame, text="Create Record", command=self.create_record).grid(row=len(create_attributes), column=0, columnspan=2, pady=10)

    def read_panel(self):
        self.read_frame = ttk.Frame(self.operation_frame)
    
        create_attributes = ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                             "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                             "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                             "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                             "AcceptedCmp2", "Complain", "Response"]

        # Create a frame for the treeview and scrollbars
        tree_frame = ttk.Frame(self.read_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Create the treeview
        self.tree = ttk.Treeview(tree_frame, columns=create_attributes, show="headings", height=20)
        for col in create_attributes:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Create horizontal scrollbar
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)

        # Grid layout for treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        # Configure the tree_frame grid
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        ttk.Button(self.read_frame, text="Refresh Data", command=self.refresh_data).pack(pady=10)

    def update_panel(self):
        self.update_frame = ttk.Frame(self.operation_frame)
        
        ttk.Label(self.update_frame, text="ID to update:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.update_id_entry = ttk.Entry(self.update_frame)
        self.update_id_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")

        create_attributes = ["Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                             "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                             "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                             "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                             "AcceptedCmp2", "Complain", "Response"]

        self.update_entries = {}
        for i, attr in enumerate(create_attributes, start=1):
            ttk.Label(self.update_frame, text=attr).grid(row=i, column=0, padx=5, pady=2, sticky="e")
            self.update_entries[attr] = ttk.Entry(self.update_frame)
            self.update_entries[attr].grid(row=i, column=1, padx=5, pady=2, sticky="w")

        ttk.Button(self.update_frame, text="Update Record", command=self.update_record).grid(row=len(create_attributes)+1, column=0, columnspan=2, pady=10)

    def delete_panel(self):
        self.delete_frame = ttk.Frame(self.operation_frame)
        
        ttk.Label(self.delete_frame, text="ID to delete:").pack(pady=5)
        self.delete_id_entry = ttk.Entry(self.delete_frame)
        self.delete_id_entry.pack(pady=5)

        ttk.Button(self.delete_frame, text="Delete Record", command=self.delete_record).pack(pady=10)

    def show_create_panel(self):
        self.clear_operation_frame()
        self.create_frame.pack(fill=tk.BOTH, expand=True)

    def show_read_panel(self):
        self.clear_operation_frame()
        self.read_frame.pack(fill=tk.BOTH, expand=True)
        self.refresh_data()

    def show_update_panel(self):
        self.clear_operation_frame()
        self.update_frame.pack(fill=tk.BOTH, expand=True)

    def show_delete_panel(self):
        self.clear_operation_frame()
        self.delete_frame.pack(fill=tk.BOTH, expand=True)

    def clear_operation_frame(self):
        for widget in self.operation_frame.winfo_children():
            widget.pack_forget()

    def create_visualization_tab(self):
        viz_frame = ttk.Frame(self.notebook)
        self.notebook.add(viz_frame, text="Data Visualization")

        viz_functions = [
            ("Age Distribution", DataViz.do_thi_phan_bo_do_tuoi),
            ("Purchase Frequency", DataViz.do_thi_luot_mua_hang),
            ("Purchase Methods", DataViz.bieu_do_phan_tich_hinh_thuc_mua_hang),
            ("Web Visits", DataViz.do_thi_so_luot_truy_cap_web),
            ("Customer Loyalty", DataViz.do_thi_phan_bo_thoi_gian_gan_bo),
            ("Annual Spending", DataViz.do_thi_tong_chi_tieu_cac_nam),
            ("Campaign Performance", DataViz.hieu_suat_chien_dich),
            ("Offer Campaigns", DataViz.chien_dich_uu_dai),
            ("Average Product Quantities", DataViz.so_luong_trung_binh_cua_moi_san_pham),
            ("Income vs Expenditure", DataViz.so_sanh_thu_nhap_va_chi_tieu_50_khach_dau_tien),
            ("Complaints by Age", DataViz.bieu_do_phan_tich_muc_do_phan_nan),
            ("Purchase Frequency by Age", DataViz.bieu_do_tan_suat_mua_hang_theo_do_tuoi)
        ]

        for i, (text, func) in enumerate(viz_functions):
            ttk.Button(viz_frame, text=text, command=lambda f=func: self.show_visualization(f)).grid(row=i//3, column=i%3, padx=5, pady=5, sticky="nsew")

        self.canvas_frame = ttk.Frame(viz_frame)
        self.canvas_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def create_record(self):
        try:
            values = [self.create_entries[attr].get() for attr in self.create_entries]
            Create(*values)
            messagebox.showinfo("Success", "Record created successfully!")
            self.refresh_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refresh_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        df = read()
        for index, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def update_record(self):
        try:
            id_to_update = int(self.update_id_entry.get())
            new_values = [id_to_update] + [self.update_entries[attr].get() for attr in self.update_entries]
            update_row_by_id(id_to_update, new_values)
            messagebox.showinfo("Success", f"Record with ID {id_to_update} updated successfully!")
            self.refresh_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_record(self):
        try:
            id_to_delete = int(self.delete_id_entry.get())
            Delete_by_ID(id_to_delete)
            messagebox.showinfo("Success", f"Record with ID {id_to_delete} deleted successfully!")
            self.refresh_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_visualization(self, viz_function):
        plt.close('all')  # Close any existing plots
        viz_function()  # Call the visualization function
        
        # Embed the plot in the tkinter window
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        
        figure = plt.gcf()
        canvas = FigureCanvasTkAgg(figure, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketingCampaignApp(root)
    root.mainloop()