import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle("Packet Data")

        # Main widget to contain the three widgets
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        
        # Vertical layout for the three widgets
        layout = QVBoxLayout(main_widget)

        # Ana sistem widget'ı
        ana_sistem_frame = QFrame()
        ana_sistem_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        ana_sistem_label = QLabel(ana_sistem_frame)
        ana_sistem_label.setText("Paket: ")
        ana_sistem_value = QLabel(ana_sistem_frame)
        layout1 = QHBoxLayout(ana_sistem_frame)
        layout1.addWidget(ana_sistem_label)
        layout1.addWidget(ana_sistem_value)
        layout.addWidget(ana_sistem_frame)

        # Yedek sistem widget'ı
        yedek_sistem_frame = QFrame()
        yedek_sistem_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        yedek_sistem_label = QLabel(yedek_sistem_frame)
        yedek_sistem_label.setText("Takım ID: ")
        yedek_sistem_value = QLabel(yedek_sistem_frame)
        layout2 = QHBoxLayout(yedek_sistem_frame)
        layout2.addWidget(yedek_sistem_label)
        layout2.addWidget(yedek_sistem_value)
        layout.addWidget(yedek_sistem_frame)

        # Faydalı yük widget'ı
        faydali_yuk_frame = QFrame()
        faydali_yuk_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        faydali_yuk_label = QLabel(faydali_yuk_frame)
        faydali_yuk_label.setText("Irtifa: ")
        faydali_yuk_value = QLabel(faydali_yuk_frame)
        layout3 = QHBoxLayout(faydali_yuk_frame)
        layout3.addWidget(faydali_yuk_label)
        layout3.addWidget(faydali_yuk_value)
        layout.addWidget(faydali_yuk_frame)

        # Ivmex widget'ı
        ivmex_frame = QFrame()
        ivmex_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        ivmex_label = QLabel(ivmex_frame)
        ivmex_label.setText("Ivme: ")
        ivmex_value = QLabel(ivmex_frame)
        layout4 = QHBoxLayout(ivmex_frame)
        layout4.addWidget(ivmex_label)
        layout4.addWidget(ivmex_value)
        layout.addWidget(ivmex_frame)

        # Display the packet data
        packet = ["Packet 1", "Takim ID 1", "1000 m", "10 m/s^2"]
        paket, takimid, irtifa, ivmex = packet

        ana_sistem_value.setText(paket)
        yedek_sistem_value.setText(takimid)
        faydali_yuk_value.setText(irtifa)
        ivmex_value.setText(ivmex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())