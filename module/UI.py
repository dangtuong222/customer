import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_visualization
import CRUD

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class MarketingCampaignUI:
    def __init__(self, master):
        self.master = master
        master.title("Marketing Campaign Analysis")
        master.geometry("1000x600")
        master.resizable(False, False)

        # Create a style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 10))
        style.configure('TNotebook.Tab', font=('Arial', 10))

        # Create main frame
        main_frame = ttk.Frame(master)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a notebook for categorized buttons
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Create categories
        categories = {
            "Customer Analysis": [
                ("Phân bố độ tuổi", data_visualization.do_thi_phan_bo_do_tuoi),
                ("Thâm niên khách hàng", data_visualization.do_thi_dtf_tham_nien_khach_hang),
                ("Phân bố thời gian gắn bó", data_visualization.do_thi_phan_bo_thoi_gian_gan_bo)
            ],
            "Purchase Behavior": [
                ("CDF Tổng số mua hàng", data_visualization.do_thi_CDF_tong_so_mua_hang),
                ("Lượt mua hàng", data_visualization.do_thi_luot_mua_hang),
                ("Phân tích hình thức mua hàng", data_visualization.bieu_do_phan_tich_hinh_thuc_mua_hang)
            ],
            "Web Activity": [
                ("Số lượt truy cập web", data_visualization.do_thi_so_luot_truy_cap_web),
                ("CDF truy cập web", data_visualization.do_thi_CDF_truy_cap_web)
            ],
            "Financial Analysis": [
                ("Tổng chi tiêu các năm", data_visualization.do_thi_tong_chi_tieu_cac_nam),
                ("Số lượng trung bình sản phẩm", data_visualization.bieu_do_so_luong_trung_binh_cua_tung_loai_san_pham)
            ],
            "Campaign Performance": [
                ("Hiệu suất chiến dịch", data_visualization.hieu_suat_chien_dich),
                ("Chiến dịch ưu đãi", data_visualization.chien_dich_uu_dai)
            ]
        }

        for category, buttons in categories.items():
            frame = ScrollableFrame(self.notebook)
            self.notebook.add(frame, text=category)
            for text, command in buttons:
                self.create_button(frame.scrollable_frame, text, command)

        # Create a frame for the plot
        self.plot_frame = ttk.Frame(main_frame)
        self.plot_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    def create_button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=lambda: self.show_plot(command))
        button.pack(fill=tk.X, padx=5, pady=5)

    def show_plot(self, plot_function):
        # Clear previous plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        # Call the plot function
        plot_function()

        # Embed the plot in tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def main():
    root = tk.Tk()
    app = MarketingCampaignUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()