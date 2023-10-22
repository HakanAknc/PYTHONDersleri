import tkinter as tk

# Ana pencere oluştur
root = tk.Tk()
root.geometry("400x300")

# Ana sistem widget'ı
ana_sistem_frame = tk.LabelFrame(root, text="Ana Sistem")
ana_sistem_frame.pack(fill="both", expand="yes", padx=20, pady=10)
ana_sistem_label = tk.Label(ana_sistem_frame, text="ANA SİSTEM")
ana_sistem_label.pack(padx=10, pady=10)

# Yedek sistem widget'ı
yedek_sistem_frame = tk.LabelFrame(root, text="Yedek Sistem")
yedek_sistem_frame.pack(fill="both", expand="yes", padx=20, pady=10)
yedek_sistem_label = tk.Label(yedek_sistem_frame, text="YEDEK SİSTEM")
yedek_sistem_label.pack(padx=10, pady=10)

# Faydalı yük widget'ı
faydali_yuk_frame = tk.LabelFrame(root, text="Faydalı Yük")
faydali_yuk_frame.pack(fill="both", expand="yes", padx=20, pady=10)
faydali_yuk_label = tk.Label(faydali_yuk_frame, text="FAYDALI YÜK")
faydali_yuk_label.pack(padx=10, pady=10)

# Ana pencereyi çalıştır
root.mainloop()