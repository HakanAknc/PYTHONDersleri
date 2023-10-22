import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("Bozdoğan Yazılım")

        # Main widget to contain the three widgets horizontally
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Horizontal layout for the three widgets
        layout = QHBoxLayout(main_widget)

        # Ana sistem widget'ı
        ana_sistem_frame = QFrame()
        ana_sistem_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        ana_sistem_layout = QVBoxLayout(ana_sistem_frame)
        ana_sistem_label = QLabel("ANA SİSTEM:")
        ana_sistem_layout.addWidget(ana_sistem_label)
        ana_sistem_layout.addWidget(QLabel("Paket:"))
        ana_sistem_layout.addWidget(QLabel("Takım ID:"))
        ana_sistem_layout.addWidget(QLabel("İrtifa:"))
        ana_sistem_layout.addWidget(QLabel("İvme:"))
        layout.addWidget(ana_sistem_frame)

        # Yedek sistem widget'ı
        yedek_sistem_frame = QFrame()
        yedek_sistem_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        yedek_sistem_layout = QVBoxLayout(yedek_sistem_frame)
        yedek_sistem_label = QLabel("YEDEK SİSTEM:")
        yedek_sistem_layout.addWidget(yedek_sistem_label)
        yedek_sistem_layout.addWidget(QLabel("Paket:"))
        yedek_sistem_layout.addWidget(QLabel("Takım ID:"))
        yedek_sistem_layout.addWidget(QLabel("İrtifa:"))
        yedek_sistem_layout.addWidget(QLabel("İvme:"))
        layout.addWidget(yedek_sistem_frame)

        # Faydalı yük widget'ı
        faydali_yuk_frame = QFrame()
        faydali_yuk_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        faydali_yuk_layout = QVBoxLayout(faydali_yuk_frame)
        faydali_yuk_label = QLabel("FAYDALI YÜK:")
        faydali_yuk_layout.addWidget(faydali_yuk_label)
        faydali_yuk_layout.addWidget(QLabel("Paket:"))
        faydali_yuk_layout.addWidget(QLabel("Takım ID:"))
        faydali_yuk_layout.addWidget(QLabel("İrtifa:"))
        faydali_yuk_layout.addWidget(QLabel("İvme:"))
        layout.addWidget(faydali_yuk_frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())