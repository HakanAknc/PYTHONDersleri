#ArayuzDeneme12 başarılı veri alınıyor
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QLineEdit, QGridLayout
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Bozdoğan Yazılım")

        # Main widget to contain the three widgets horizontally
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Horizontal layout for the three widgets
        layout = QHBoxLayout(main_widget)

        layout.setSpacing(20)

        self.widget1 = self.create_sistem_widget("ANA SİSTEM:")
        self.widget2 = self.create_sistem_widget("YEDEK SİSTEM:")
        self.widget3 = self.create_sistem_widget("FAYDALI YÜK:")

        layout.addWidget(self.widget1)
        layout.addWidget(self.widget2)
        layout.addWidget(self.widget3)

        # Set up timer to update values every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(1000)

    def create_sistem_widget(self, sistem_adi):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QGridLayout(frame)

        label = QLabel(sistem_adi)
        label.setStyleSheet("font-weight: bold")

        layout.addWidget(label, 0, 0)

        ana_paket = QLineEdit()
        ana_paket.setReadOnly(True)
        ana_paket.setObjectName("paket")
        layout.addWidget(QLabel("Paket (m):"), 1, 0)
        layout.addWidget(ana_paket, 1, 1)

        ana_ivme = QLineEdit()
        ana_ivme.setReadOnly(True)
        ana_ivme.setObjectName("ivme")
        layout.addWidget(QLabel("İvme (m/s²):"), 2, 0)
        layout.addWidget(ana_ivme, 2, 1)

        ana_irtifa = QLineEdit()
        ana_irtifa.setReadOnly(True)
        ana_irtifa.setObjectName("irtifa")
        layout.addWidget(QLabel("İrtifa (m):"), 3, 0)
        layout.addWidget(ana_irtifa, 3, 1)

        ana_sicaklik = QLineEdit()
        ana_sicaklik.setReadOnly(True)
        ana_sicaklik.setObjectName("sicaklik")
        layout.addWidget(QLabel("Sıcaklık (°C):"), 4, 0)
        layout.addWidget(ana_sicaklik, 4, 1)

        ana_nem = QLineEdit()
        ana_nem.setReadOnly(True)
        ana_nem.setObjectName("nem")
        layout.addWidget(QLabel("Nem (%):"), 5, 0)
        layout.addWidget(ana_nem, 5, 1)

        frame.setLayout(layout)

        return frame

    def update_values(self):
        # Generate random values for each parameter
        faydali_yuk_paket = round(random.uniform(0, 10), 2)
        faydali_yuk_ivme = round(random.uniform(0, 5), 2)
        faydali_yuk_irtifa = round(random.uniform(0, 500), 2)
        faydali_yuk_sicaklik = round(random.uniform(-50, 50), 2)
        faydali_yuk_nem = round(random.uniform(0, 100), 2)

        ana_sistem_paket = round(random.uniform(0, 10), 2)
        ana_sistem_ivme = round(random.uniform(0, 5), 2)
        ana_sistem_irtifa = round(random.uniform(0, 500), 2)
        ana_sistem_sicaklik = round(random.uniform(-50, 50), 2)
        ana_sistem_nem = round(random.uniform(0, 100), 2)

        yedek_sistem_paket = round(random.uniform(0, 10), 2)
        yedek_sistem_ivme = round(random.uniform(0, 5), 2)
        yedek_sistem_irtifa = round(random.uniform(0, 500), 2)
        yedek_sistem_sicaklik = round(random.uniform(-50, 50), 2)
        yedek_sistem_nem = round(random.uniform(0, 100), 2)

        # Update the values in the UI
        self.widget1.findChild(QLineEdit, "paket").setText(str(ana_sistem_paket))
        self.widget1.findChild(QLineEdit, "ivme").setText(str(ana_sistem_ivme))
        self.widget1.findChild(QLineEdit, "irtifa").setText(str(ana_sistem_irtifa))
        self.widget1.findChild(QLineEdit, "sicaklik").setText(str(ana_sistem_sicaklik))
        self.widget1.findChild(QLineEdit, "nem").setText(str(ana_sistem_nem))

        self.widget2.findChild(QLineEdit, "paket").setText(str(yedek_sistem_paket))
        self.widget2.findChild(QLineEdit, "ivme").setText(str(yedek_sistem_ivme))
        self.widget2.findChild(QLineEdit, "irtifa").setText(str(yedek_sistem_irtifa))
        self.widget2.findChild(QLineEdit, "sicaklik").setText(str(yedek_sistem_sicaklik))
        self.widget2.findChild(QLineEdit, "nem").setText(str(yedek_sistem_nem))

        self.widget3.findChild(QLineEdit, "paket").setText(str(faydali_yuk_paket))
        self.widget3.findChild(QLineEdit, "ivme").setText(str(faydali_yuk_ivme))
        self.widget3.findChild(QLineEdit, "irtifa").setText(str(faydali_yuk_irtifa))
        self.widget3.findChild(QLineEdit, "sicaklik").setText(str(faydali_yuk_sicaklik))
        self.widget3.findChild(QLineEdit, "nem").setText(str(faydali_yuk_nem))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# bu dosyayı deneme03 dosyasına ekle