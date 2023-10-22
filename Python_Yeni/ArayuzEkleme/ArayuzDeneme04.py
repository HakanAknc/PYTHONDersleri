import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QFrame

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
        ana_sistem_label = QLabel(ana_sistem_frame)
        ana_sistem_label.setText("ANA SİSTEM:")
        layout.addWidget(ana_sistem_frame)

        # Yedek sistem widget'ı
        yedek_sistem_frame = QFrame()
        yedek_sistem_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        yedek_sistem_label = QLabel(yedek_sistem_frame)
        yedek_sistem_label.setText("YEDEK SİSTEM:")
        layout.addWidget(yedek_sistem_frame)

        # Faydalı yük widget'ı
        faydali_yuk_frame = QFrame()
        faydali_yuk_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        faydali_yuk_label = QLabel(faydali_yuk_frame)
        faydali_yuk_label.setText("FAYDALI YÜK:")
        layout.addWidget(faydali_yuk_frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())