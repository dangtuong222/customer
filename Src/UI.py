import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from CRUD.Create import Create
from CRUD.Read import read
from CRUD.Delete import Delete_by_ID
from CRUD.Update import update_row_by_id
from CRUD.Find import find_by_id
import Data_visualization as DataViz
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
class MarketingCampaignApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Marketing Campaign Analysis")
        self.master.geometry("1200x800")
        self.master.configure(bg="#f0f0f0")  

        self.style = ttk.Style()
        self.style.theme_use("clam")  
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", background="#4a7abc", foreground="white", font=("Arial", 10, "bold"))
        self.style.map("TButton", background=[("active", "#3a5a8c")])
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TEntry", fieldbackground="white", font=("Arial", 10))
        self.style.configure("TCombobox", fieldbackground="white", font=("Arial", 10))
        self.style.configure("Treeview", background="white", fieldbackground="white", font=("Arial", 9))
        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        # Tạo Notebook để chứa các tab
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Tạo các tab khác nhau trong ứng dụng
        self.create_crud_tab()
        self.create_visualization_tab()
        
    def create_crud_tab(self):
        # Tab CRUD Operations
        crud_frame = ttk.Frame(self.notebook)
        self.notebook.add(crud_frame, text="CRUD Operations")
        
        button_frame = ttk.Frame(crud_frame)
        button_frame.pack(pady=10)
        try:
            # Thay đổi lại đường dẫn hình ảnh cho phù hợp với thiết bị
            logo_image = Image.open(r"D:\python\PROJECT\Logo\logo.png") 
            logo_image = logo_image.resize((50, 50)) 
            logo = ImageTk.PhotoImage(logo_image)
            logo_label = ttk.Label(button_frame, image=logo)
            logo_label.image = logo 
            logo_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        except FileNotFoundError:
            print("Logo image not found. Please check the path.")

        # Thêm các nút chức năng bên cạnh logo
        operations = [("Create", self.show_create_panel),
                    ("Read", self.show_read_panel),
                    ("Update", self.show_update_panel),
                    ("Delete", self.show_delete_panel),
                    ("Search", self.show_Search_panel)]

        for i, (text, command) in enumerate(operations):
            ttk.Button(button_frame, text=text, command=command, style="TButton").grid(row=0, column=i + 1, padx=5)

        # Frame để chứa các thao tác CRUD
        self.operation_frame = ttk.Frame(crud_frame)
        self.operation_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Tạo các bảng giao diện CRUD
        self.create_panel()
        self.read_panel()
        self.update_panel()
        self.delete_panel()
        self.Search_panel()
        self.show_read_panel()

    def create_panel(self):
        # Tạo giao diện cho Create Panel
        self.create_frame = ttk.Frame(self.operation_frame)
    
        # Tạo một khung chứa để bố cục chia đôi.
        container = ttk.Frame(self.create_frame)
        container.pack(fill=tk.BOTH, expand=True)
    
        # Phần bên trái - Form nhập liệu
        form_frame = ttk.Frame(container)
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        # Các thuộc tính cần nhập
        create_attributes = ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                           "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                           "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                           "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                           "AcceptedCmp2", "Complain", "Response"]

        self.create_entries = {}
        for i, attr in enumerate(create_attributes):
            ttk.Label(form_frame, text=attr).grid(row=i+1, column=0, padx=5, pady=2, sticky="e")
            if attr == "Education":
                self.create_entries[attr] = ttk.Combobox(form_frame, values=["Master", "Graduation", "PhD"])
            elif attr == "Marital_Status":
                self.create_entries[attr] = ttk.Combobox(form_frame, values=["In relationship", "Single"])
            elif attr in ["AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", "AcceptedCmp2", "Complain", "Response"]:
                self.create_entries[attr] = ttk.Combobox(form_frame, values=["0", "1"])
            elif attr == "Dt_Customer":
                self.create_entries[attr] = DateEntry(form_frame, width=12, background='#4a7abc', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
            else:
                self.create_entries[attr] = ttk.Entry(form_frame)
            self.create_entries[attr].grid(row=i+1, column=1, padx=5, pady=2, sticky="w")

        ttk.Button(form_frame, text="Create Record", command=self.create_record, style="TButton").grid(row=len(create_attributes)+1, column=0, columnspan=2, pady=10)

        # Phần bên phải - Hình ảnh/Preview
        preview_frame = ttk.Frame(container)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        try:
            logo_image = Image.open(r"D:\python\PROJECT\Logo\LOGOHCMUTE.png")
            logo_image = logo_image.resize((550, 550))
            # Làm sắc nét hình ảnh
            logof_image = logo_image.filter(ImageFilter.SHARPEN)
            logo = ImageTk.PhotoImage(logof_image)
            logo_label = ttk.Label(preview_frame, image=logo)
            logo_label.image = logo
            logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        except FileNotFoundError:
            print("Logo image not found. Please check the path.")
    
    def read_panel(self):
        self.read_frame = ttk.Frame(self.operation_frame)
    
        create_attributes = ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                             "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                             "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                             "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                             "AcceptedCmp2", "Complain", "Response"]

        # Tạo giao diện cho Read Panel
        tree_frame = ttk.Frame(self.read_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo chế độ xem dạng cây
        self.tree = ttk.Treeview(tree_frame, columns=create_attributes, show="headings", height=20)
        for col in create_attributes:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Tạo thanh cuộn dọc
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Tạo thanh cuộn ngang
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)

        # Bố cục lưới cho chế độ xem dạng cây và thanh cuộn
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        # Định cấu hình lưới tree_frame
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        ttk.Button(self.read_frame, text="Refresh Data", command=self.refresh_data).pack(pady=10)

    def update_panel(self):
        self.update_frame = ttk.Frame(self.operation_frame)
        container = ttk.Frame(self.update_frame)
        container.pack(fill=tk.BOTH, expand=True)
        
        form_frame = ttk.Frame(container)
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        ttk.Label(form_frame, text="ID to update:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.update_id_entry = ttk.Entry(form_frame)
        self.update_id_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")

        create_attributes = ["Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                             "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                             "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                             "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                             "AcceptedCmp2", "Complain", "Response"]

        self.update_entries = {}
        for i, attr in enumerate(create_attributes, start=1):
            ttk.Label(form_frame, text=attr).grid(row=i, column=0, padx=5, pady=2, sticky="e")
            if attr == "Education":
                self.update_entries[attr] = ttk.Combobox(form_frame, values=["Master", "Graduation", "PhD"])
            elif attr == "Marital_Status":
                self.update_entries[attr] = ttk.Combobox(form_frame, values=["In relationship", "Single"])
            elif attr in ["AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", "AcceptedCmp2", "Complain", "Response"]:
                self.update_entries[attr] = ttk.Combobox(form_frame, values=["0", "1"])
            elif attr == "Dt_Customer":
                self.update_entries[attr] = DateEntry(form_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
            else:
                self.update_entries[attr] = ttk.Entry(form_frame)
            self.update_entries[attr].grid(row=i, column=1, padx=5, pady=2, sticky="w")

        ttk.Button(form_frame, text="Update Record", command=self.update_record).grid(row=len(create_attributes)+1, column=0, columnspan=2, pady=10)
        
        preview_frame = ttk.Frame(container)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        try:
            logo_image = Image.open(r"D:\python\PROJECT\Logo\LOGOHCMUTE.png")
            logo_image = logo_image.resize((550, 550))
            # # Làm sắc nét hình ảnh
            logof_image = logo_image.filter(ImageFilter.SHARPEN)
            logo = ImageTk.PhotoImage(logof_image)
            logo_label = ttk.Label(preview_frame, image=logo)
            logo_label.image = logo
            logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        except FileNotFoundError:
            print("Logo image not found. Please check the path.")
            
    def delete_panel(self):
        self.delete_frame = ttk.Frame(self.operation_frame)
        
        ttk.Label(self.delete_frame, text="ID to delete:").pack(pady=5)
        self.delete_id_entry = ttk.Entry(self.delete_frame)
        self.delete_id_entry.pack(pady=5)

        ttk.Button(self.delete_frame, text="Delete Record", command=self.delete_record).pack(pady=10)

    def Search_panel(self):
        self.Search_frame = ttk.Frame(self.operation_frame)
        
        search_input_frame = ttk.Frame(self.Search_frame)
        search_input_frame.pack(pady=10)

        ttk.Label(search_input_frame, text="ID to Search:").pack(side=tk.LEFT, padx=5)
        self.Search_id_entry = ttk.Entry(search_input_frame)
        self.Search_id_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(search_input_frame, text="Search Record", command=self.Search_record).pack(side=tk.LEFT, padx=5)

        tree_frame = ttk.Frame(self.Search_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Dt_Customer", "Recency", "MntWines",
                   "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 
                   "NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", 
                   "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", 
                   "AcceptedCmp2", "Complain", "Response"]

        self.search_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.search_tree.heading(col, text=col)
            self.search_tree.column(col, width=100)

        # Tạp thanh cuộn dọc và ngang
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.search_tree.yview)
        self.search_tree.configure(yscrollcommand=vsb.set)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.search_tree.xview)
        self.search_tree.configure(xscrollcommand=hsb.set)

        self.search_tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

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
        
    def show_Search_panel(self):
        self.clear_operation_frame()
        self.Search_frame.pack(fill=tk.BOTH, expand=True)
        
    def clear_operation_frame(self):
        for widget in self.operation_frame.winfo_children():
            widget.pack_forget()

    def create_visualization_tab(self):
        viz_frame = ttk.Frame(self.notebook)
        self.notebook.add(viz_frame, text="Data Visualization")

        button_frame = ttk.Frame(viz_frame)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        viz_functions = [
            ("Age Distribution", DataViz.do_thi_phan_bo_do_tuoi),
            ("Web Visits", DataViz.do_thi_so_luot_truy_cap_web),
            ("Annual Spending", DataViz.do_thi_tong_chi_tieu_cac_nam),
            ("Campaign Performance", DataViz.hieu_suat_chien_dich),
            ("Number of customers accepting the offer", DataViz.so_khach_hang_chap_nhan_uu_dai),
            ("Average Product Quantities", DataViz.so_luong_trung_binh_cua_moi_san_pham),
            ("Complaints by Age", DataViz.bieu_do_phan_tich_muc_do_phan_nan),
            ("Purchase Frequency by Age", DataViz.bieu_do_tan_suat_mua_hang_theo_do_tuoi)
        ]

        for text, func in viz_functions:
            button = ttk.Button(button_frame, text=text, command=lambda f=func: self.show_visualization(f), style="TButton")
            button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            button.configure(width=20)

        self.canvas_frame = ttk.Frame(viz_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_record(self):
        values = []
        for attr, entry in self.create_entries.items():
            if attr == "Dt_Customer":
                date_value = entry.get_date().strftime("%Y-%m-%d")
                values.append(date_value)
            else:
                values.append(entry.get())
        Create(*values)
        self.refresh_data()
    
    def refresh_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        df = read()
        for index, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def update_record(self):
        id_to_update = int(self.update_id_entry.get())
        new_values = [id_to_update]
        for attr, entry in self.update_entries.items():
            if attr == "Dt_Customer":
                date_value = entry.get_date().strftime("%Y-%m-%d")
                new_values.append(date_value)
            else:
                new_values.append(entry.get())
        update_row_by_id(id_to_update, new_values)
        self.refresh_data()

    def delete_record(self):
        id_to_delete = int(self.delete_id_entry.get())
        Delete_by_ID(id_to_delete)
        self.refresh_data()
        
    def Search_record(self):
        id_to_search = int(self.Search_id_entry.get())
        record = find_by_id(id_to_search)
            
        # Clear previous results
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
            
        if record is not None:
            # Display the record in the treeview
            self.search_tree.insert("", "end", values=list(record))

    def show_visualization(self, viz_function):
        plt.close('all')
        viz_function()
        
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        
        figure = plt.gcf()
        canvas = FigureCanvasTkAgg(figure, master=self.canvas_frame)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Thêm hiệu ứng
        self.animate_widget(canvas_widget)

    def animate_widget(self, widget):
        def fade_in(alpha):
            widget.configure(style=f"Fade.TFrame")
            self.style.configure(f"Fade.TFrame", background=f"#{int(240*alpha):02x}{int(240*alpha):02x}{int(240*alpha):02x}")
            if alpha < 1:
                self.master.after(20, lambda: fade_in(min(alpha + 0.1, 1)))
        fade_in(0)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MarketingCampaignApp(root)
    root.mainloop()