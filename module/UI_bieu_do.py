import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_visualization
import data_cleaning
import data_connection

class DataVisualizationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Biểu đồ")
        self.master.geometry("800x600")

        # Frame cho các nút
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Frame cho biểu đồ
        self.chart_frame = ttk.Frame(self.master)
        self.chart_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.current_canvas = None
        self.current_figure = None

        self.create_buttons()

    def create_buttons(self):
        ttk.Button(self.button_frame, text="Mức độ phàn nàn theo độ tuổi", command=self.show_complaint_chart).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Tỷ lệ chấp nhận chiến dịch", command=self.show_campaign_chart).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Tần suất mua hàng theo độ tuổi", command=self.show_purchase_frequency_chart).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Hình thức mua hàng", command=self.show_purchase_channels_chart).pack(side=tk.LEFT, padx=5)

    def clear_chart_frame(self):
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        if self.current_canvas:
            self.current_canvas.get_tk_widget().destroy()
        
        if self.current_figure:
            plt.close(self.current_figure)

    def show_chart(self, chart_function, title):
        self.clear_chart_frame()
        
        self.current_figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = self.current_figure.add_subplot(111)
        
        chart_function()
        
        self.current_canvas = FigureCanvasTkAgg(self.current_figure, master=self.chart_frame)
        self.current_canvas.draw()
        self.current_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        label = ttk.Label(self.chart_frame, text=title, font=("Arial", 16))
        label.pack(pady=5)

    def show_complaint_chart(self):
        self.show_chart(data_visualization.bieu_do_phan_tich_muc_do_phan_nan, "Mức độ phàn nàn theo độ tuổi")

    def show_campaign_chart(self):
        self.show_chart(data_visualization.bieu_do_phan_tich_ty_le_chap_nhan_chien_dich_cua_khach_hang, "Tỷ lệ chấp nhận chiến dịch")

    def show_purchase_frequency_chart(self):
        self.show_chart(data_visualization.bieu_do_tan_suat_mua_hang_theo_do_tuoi, "Tần suất mua hàng theo độ tuổi")

    def show_purchase_channels_chart(self):
        self.show_chart(data_visualization.bieu_do_tron_phan_tich_hinh_thuc_mua_hang, "Hình thức mua hàng")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizationGUI(root)
    root.mainloop()