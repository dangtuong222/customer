import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ChartViewer:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        self.create_chart_window()

    def create_chart_window(self):
        """Tạo cửa sổ để hiển thị biểu đồ trong Tkinter."""
        chart_frame = tk.Frame(self.root)
        chart_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Tạo menu lựa chọn biểu đồ
        chart_menu = ttk.Combobox(chart_frame, values=["Age Group Distribution", "Income vs Expenditure", "Web Visits Distribution"], state="readonly")
        chart_menu.set("Select Chart")
        chart_menu.pack(side="top", pady=10)
        
        # Nút để vẽ biểu đồ
        show_button = tk.Button(chart_frame, text="Show Chart", command=lambda: self.show_chart(chart_menu.get()))
        show_button.pack(side="top", pady=5)

    def show_chart(self, chart_type):
        """Hiển thị biểu đồ dựa trên lựa chọn của người dùng."""
        if chart_type == "Age Group Distribution":
            self.bieu_do_phan_bo_do_tuoi()
        elif chart_type == "Income vs Expenditure":
            self.bieu_do_so_sanh_chi_tieu_va_thu_nhap()
        elif chart_type == "Web Visits Distribution":
            self.bieu_do_phan_phoi_luot_truy_cap_web()
        else:
            messagebox.showerror("Error", "Invalid chart selection!")

    def bieu_do_phan_bo_do_tuoi(self):
        """Vẽ biểu đồ phân bổ độ tuổi theo các nhóm tuổi."""
        fig = plt.figure(figsize=(10, 6))  # Create a new figure for this chart
        current_year = datetime.now().year
        self.df['Age'] = current_year - self.df['Year_Birth']  # Calculate ages

        bins = [0, 25, 35, 45, 55, 65, 75, 100]
        labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']
        self.df['Age_Group'] = pd.cut(self.df['Age'], bins=bins, labels=labels, right=False)
        age_group_counts = self.df['Age_Group'].value_counts().sort_index()

        ax = fig.add_subplot(111)
        age_group_counts.plot(kind='bar', color='salmon', edgecolor='black', ax=ax)
        ax.set_title("Age Group Distribution")
        ax.set_xlabel("Age Group")
        ax.set_ylabel("Number of Customers")
        ax.set_xticklabels(age_group_counts.index, rotation=45)
        plt.tight_layout()

        self.display_chart(fig)

    def bieu_do_so_sanh_chi_tieu_va_thu_nhap(self):
        """Vẽ biểu đồ so sánh tổng chi tiêu và thu nhập của 50 khách hàng đầu tiên."""
        fig = plt.figure(figsize=(10, 6))  # Create a new figure for this chart
        product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        self.df['Total_Expenditure'] = self.df[product_columns].sum(axis=1)
        
        self.df = self.df.dropna(subset=['Income'])
        self.df['Income'] = self.df['Income'].astype(float)
        sample_data = self.df.head(50)

        ax = fig.add_subplot(111)
        ax.bar(sample_data.index - 0.2, sample_data['Income'], width=0.4, label='Total Income', color='blue')
        ax.bar(sample_data.index + 0.2, sample_data['Total_Expenditure'], width=0.4, label='Total Expenditure', color='red')
        ax.set_title('Comparison of Total Income and Total Expenditure (First 50 Customers)')
        ax.set_xlabel('Customer Index')
        ax.set_ylabel('Amount')
        ax.legend()
        plt.tight_layout()

        self.display_chart(fig)

    def bieu_do_phan_phoi_luot_truy_cap_web(self):
        """Vẽ biểu đồ phân phối lượt truy cập web theo tháng."""
        fig = plt.figure(figsize=(10, 6))  # Create a new figure for this chart
        web_visits = self.df['NumWebVisitsMonth']

        ax = fig.add_subplot(111)
        ax.hist(web_visits, bins=10, color='skyblue', edgecolor='black')
        ax.set_title('Distribution of Web Visits per Month')
        ax.set_xlabel('Number of Web Visits in a Month')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        self.display_chart(fig)

    def display_chart(self, fig):
        """Hiển thị biểu đồ lên một cửa sổ mới trong Tkinter."""
        new_window = Toplevel(self.root)
        new_window.title("Chart Viewer")
        new_window.geometry("800x600")

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

class Create:
    def __init__(self, root, tree, df):
        self.root = root
        self.tree = tree
        self.df = df
        self.create_window()

    def create_window(self):
        """Tạo cửa sổ nhập liệu dữ liệu mới."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Create New Entry")
        
        # Điều chỉnh kích thước cửa sổ
        self.window.geometry("600x400")  

        # Tạo Canvas cho thanh cuộn
        canvas = tk.Canvas(self.window)
        canvas.pack(side="left", fill="both", expand=True)

        # Tạo thanh cuộn dọc
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Tạo một frame trong canvas
        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Các nhãn và ô nhập liệu
        self.labels = []
        self.entries = []

        for col in self.df.columns:
            label = tk.Label(scrollable_frame, text=col)
            label.grid(row=len(self.labels), column=0, padx=10, pady=5, sticky="w")
            self.labels.append(label)
            
            entry = tk.Entry(scrollable_frame, width=40)
            entry.grid(row=len(self.entries), column=1, padx=10, pady=5)
            self.entries.append(entry)

        # Nút lưu
        save_button = tk.Button(scrollable_frame, text="Save", command=self.save_data)
        save_button.grid(row=len(self.df.columns), column=0, columnspan=2, pady=10)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def save_data(self):
        """Lưu dữ liệu từ các ô nhập liệu vào DataFrame và CSV."""
        # Kiểm tra và thay thế ô trống bằng "Chưa có thông tin"
        new_data = [entry.get().strip() if entry.get().strip() != "" else "Chưa có thông tin" for entry in self.entries]
        
        # Cập nhật DataFrame
        new_row = pd.Series(new_data, index=self.df.columns)
        self.df = pd.concat([self.df, new_row.to_frame().T], ignore_index=True)
        
        # Lưu lại vào CSV
        self.df.to_csv('marketing_campaign.csv', sep=';', index=False)

        # Làm mới Treeview bằng cách gọi callback update_treeview
        self.reload_treeview()

        # Đóng cửa sổ
        self.window.destroy()

    def reload_treeview(self):
        """Làm mới Treeview sau khi thêm dữ liệu."""
        # Xóa dữ liệu hiện tại trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Chèn lại tất cả dữ liệu từ DataFrame vào Treeview
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

class Search:
    def __init__(self, root, tree, df):
        self.root = root
        self.tree = tree
        self.df = df
        self.create_search_window()

    def create_search_window(self):
        """Tạo cửa sổ tìm kiếm theo ID."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Tìm kiếm theo ID")

        self.label = tk.Label(self.window, text="Nhập ID để tìm kiếm:")
        self.label.pack(padx=10, pady=10)

        self.search_entry = tk.Entry(self.window, width=30)
        self.search_entry.pack(padx=10, pady=10)

        self.search_button = tk.Button(self.window, text="Tìm kiếm", command=self.search_data)
        self.search_button.pack(pady=10)

    def search_data(self):
        """Tìm kiếm dữ liệu theo ID."""
        search_id = self.search_entry.get().strip()

        # Đảm bảo ID là chuỗi và không có khoảng trắng thừa
        self.df['ID'] = self.df['ID'].astype(str).str.strip()

        print(f"Searching for ID: {search_id}")  # Debugging: In ra ID tìm kiếm

        rows = self.df[self.df['ID'] == search_id]
        
        # Xóa dữ liệu hiện tại trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not rows.empty:
            # Chèn dữ liệu vào Treeview
            for _, row_data in rows.iterrows():
                self.tree.insert("", "end", values=list(row_data))
        else:
            # Hiển thị thông báo nếu không tìm thấy dữ liệu
            self.show_message("Không tìm thấy dữ liệu cho ID đã nhập.")

    def show_message(self, message):
        """Hiển thị thông báo kết quả tìm kiếm."""
        messagebox.showinfo("Kết quả tìm kiếm", message)

class Delete:
    def __init__(self, root, tree, df):
        self.root = root
        self.tree = tree
        self.df = df
        self.create_delete_window()

    def create_delete_window(self):
        """Tạo cửa sổ xóa dữ liệu theo ID."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Delete Entry")

        self.label = tk.Label(self.window, text="Nhập ID để xóa:")
        self.label.pack(padx=10, pady=10)

        self.delete_entry = tk.Entry(self.window, width=30)
        self.delete_entry.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.window, text="Xóa", command=self.delete_data)
        self.delete_button.pack(pady=10)

    def delete_data(self):
        """Xóa dữ liệu theo ID."""
        delete_id = self.delete_entry.get().strip()

        # Đảm bảo ID là chuỗi và không có khoảng trắng thừa
        self.df['ID'] = self.df['ID'].astype(str).str.strip()

        # Kiểm tra và xóa bản ghi có ID khớp
        rows_to_delete = self.df[self.df['ID'] == delete_id]

        if not rows_to_delete.empty:
            self.df = self.df[self.df['ID'] != delete_id]
            self.df.to_csv('marketing_campaign.csv', sep=';', index=False)
            self.reload_treeview()
            self.show_message(f"Dữ liệu với ID {delete_id} đã bị xóa.")
        else:
            self.show_message("Không tìm thấy dữ liệu để xóa.")

    def reload_treeview(self):
        """Làm mới Treeview sau khi xóa dữ liệu."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def show_message(self, message):
        """Hiển thị thông báo kết quả xóa."""
        messagebox.showinfo("Kết quả xóa", message)

class Update:
    def __init__(self, root, tree, df):
        self.root = root
        self.tree = tree
        self.df = df
        self.create_update_window()

    def create_update_window(self):
        """Tạo cửa sổ cập nhật dữ liệu theo ID."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Update Entry")

        self.label = tk.Label(self.window, text="Nhập ID để cập nhật:")
        self.label.pack(padx=10, pady=10)

        self.update_entry = tk.Entry(self.window, width=30)
        self.update_entry.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.window, text="Cập nhật", command=self.update_data)
        self.update_button.pack(pady=10)

    def update_data(self):
        """Cập nhật dữ liệu theo ID."""
        update_id = self.update_entry.get().strip()

        # Đảm bảo ID là chuỗi và không có khoảng trắng thừa
        self.df['ID'] = self.df['ID'].astype(str).str.strip()

        rows_to_update = self.df[self.df['ID'] == update_id]

        if not rows_to_update.empty:
            # Tạo cửa sổ nhập liệu mới để cập nhật thông tin
            UpdateData(self.root, self.tree, self.df, update_id)
        else:
            self.show_message("Không tìm thấy dữ liệu để cập nhật.")

    def show_message(self, message):
        """Hiển thị thông báo kết quả cập nhật."""
        messagebox.showinfo("Kết quả cập nhật", message)

class UpdateData:
    def __init__(self, root, tree, df, update_id):
        self.root = root
        self.tree = tree
        self.df = df
        self.update_id = update_id
        self.create_update_data_window()

    def create_update_data_window(self):
        """Tạo cửa sổ nhập liệu để cập nhật thông tin."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Update Data")

        self.label = tk.Label(self.window, text="Cập nhật thông tin cho ID: " + self.update_id)
        self.label.pack(padx=10, pady=10)

        # Tạo Canvas và thanh cuộn dọc
        canvas = tk.Canvas(self.window)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Tạo một frame trong canvas
        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Tạo các ô nhập liệu cho mỗi cột
        self.entries = {}
        for col in self.df.columns:
            label = tk.Label(scrollable_frame, text=col)
            label.pack(padx=10, pady=5, anchor="w")
            entry = tk.Entry(scrollable_frame, width=40)
            entry.insert(0, self.df.loc[self.df['ID'] == self.update_id, col].values[0])  # Điền giá trị hiện tại
            entry.pack(padx=10, pady=5)
            self.entries[col] = entry

        # Nút lưu thay đổi
        save_button = tk.Button(scrollable_frame, text="Save", command=self.save_updated_data)
        save_button.pack(pady=10)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def save_updated_data(self):
        """Lưu thông tin cập nhật vào DataFrame và CSV."""
        updated_data = [entry.get().strip() if entry.get().strip() != "" else "Chưa có thông tin" for entry in self.entries.values()]

        # Cập nhật DataFrame
        self.df.loc[self.df['ID'] == self.update_id, :] = updated_data
        self.df.to_csv('marketing_campaign.csv', sep=';', index=False)

        # Làm mới Treeview và đóng cửa sổ
        self.reload_treeview()
        self.window.destroy()

    def reload_treeview(self):
        """Làm mới Treeview sau khi cập nhật dữ liệu."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

class Application:
    def __init__(self, root):
        self.root = root
        self.df = self.load_data()
        self.tree, self.v_scrollbar = self.create_treeview()
        self.create_buttons()

    def load_data(self):
        """Tải dữ liệu từ file CSV."""
        file_path = 'marketing_campaign.csv'
        try:
            df = pd.read_csv(file_path, sep=";")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            df = pd.DataFrame()  # Trả về DataFrame rỗng nếu có lỗi
        return df

    def create_treeview(self):
        """Tạo Treeview để hiển thị dữ liệu."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Add title above the Treeview
        title_label = tk.Label(frame, text="Marketing Campaign Dataset", font=("Helvetica", 16, "bold"))
        title_label.pack(side="top", pady=(0, 10))
        
        tree = ttk.Treeview(frame)
        tree["columns"] = list(self.df.columns)
        tree["show"] = "headings"

        for col in self.df.columns:
            max_width = max(self.df[col].astype(str).map(len).max(), len(col)) * 8
            tree.heading(col, text=col)
            tree.column(col, width=max_width, anchor="center", stretch=True)

        for _, row in self.df.iterrows():
            tree.insert("", "end", values=list(row))

        v_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=v_scrollbar.set)
        v_scrollbar.pack(side="right", fill="y")

        h_scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side="top", fill="x")

        tree.pack(side="top", fill="both", expand=True)
        return tree, v_scrollbar

    def create_buttons(self):
        """Tạo các nút chức năng."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", pady=5)

        buttons = ["Create", "Search", "Delete", "Update", "Show Chart", "Quit"]  # Thêm "Show Chart" vào đây
        for btn_text in buttons:
            button = tk.Button(button_frame, text=btn_text, width=10, command=lambda btn=btn_text: self.handle_button_click(btn))
            button.pack(side="left", padx=5)

    def handle_button_click(self, btn_text):
        """Xử lý sự kiện khi nhấn các nút."""
        if btn_text == "Create":
            Create(self.root, self.tree, self.df)
        elif btn_text == "Search":
            Search(self.root, self.tree, self.df)
        elif btn_text == "Delete":
            Delete(self.root, self.tree, self.df)
        elif btn_text == "Update":
            Update(self.root, self.tree, self.df)
        elif btn_text == "Show Chart":  # Open chart viewer
            ChartViewer(self.root, self.df)  # Ensure you pass the DataFrame to ChartViewer
        elif btn_text == "Quit":
            self.root.quit()



# Tạo cửa sổ ứng dụng chính
root = tk.Tk()
root.title("Dataset Viewer")

# Tạo ứng dụng
app = Application(root)

# Chạy ứng dụng
root.geometry("1200x600")
root.mainloop()
