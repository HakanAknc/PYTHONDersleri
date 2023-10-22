import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("GUI Window")

        self.central_widget = QFrame()
        self.setCentralWidget(self.central_widget)

        # Ana sistem widget'ı
        ana_sistem_frame = QFrame(self.central_widget)
        ana_sistem_frame.setGeometry(20, 10, 360, 90)
        ana_sistem_label = QLabel(ana_sistem_frame)
        ana_sistem_label.setGeometry(10, 10, 340, 70)
        ana_sistem_label.setText("ANA SİSTEM:")

        # Yedek sistem widget'ı
        yedek_sistem_frame = QFrame(self.central_widget)
        yedek_sistem_frame.setGeometry(20, 110, 360, 90)
        yedek_sistem_label = QLabel(yedek_sistem_frame)
        yedek_sistem_label.setGeometry(10, 10, 340, 70)
        yedek_sistem_label.setText("YEDEK SİSTEM:")

        # Faydalı yük widget'ı
        faydali_yuk_frame = QFrame(self.central_widget)
        faydali_yuk_frame.setGeometry(20, 210, 360, 90)
        faydali_yuk_label = QLabel(faydali_yuk_frame)
        faydali_yuk_label.setGeometry(10, 10, 340, 70)
        faydali_yuk_label.setText("FAYDALI YÜK:")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())