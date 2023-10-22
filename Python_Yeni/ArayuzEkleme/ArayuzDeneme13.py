#ArayuzDeneme13 başarılı bu tamamdır
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QLineEdit, QGridLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 600)
        self.setWindowTitle("Bozdoğan Yazılım")

        # Main widget to contain the widgets
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Grid layout for the widgets
        layout = QGridLayout(main_widget)
        layout.setSpacing(20)

        # Sistem widgets
        self.widget1 = self.create_sistem_widget("ANA SİSTEM:")
        self.widget2 = self.create_sistem_widget("YEDEK SİSTEM:")
        self.widget3 = self.create_sistem_widget("FAYDALI YÜK:")
        layout.addWidget(self.widget1, 0, 0)
        layout.addWidget(self.widget2, 0, 1)
        layout.addWidget(self.widget3, 1, 0, 1, 2)

        # Roket widget
        self.roket_widget = self.create_roket_widget()
        layout.addWidget(self.roket_widget, 2, 0)

        # Pil widget
        self.pil_widget = self.create_pil_widget()
        layout.addWidget(self.pil_widget, 2, 1)

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
        layout.addWidget(label, 0, 0, 1, 3)

        layout.addWidget(QLabel("Paket (m):"), 1, 0)
        layout.addWidget(QLabel("İvme (m/s²):"), 2, 0)
        layout.addWidget(QLabel("İrtifa (m):"), 3, 0)
        layout.addWidget(QLabel("Sıcaklık (°C):"), 4, 0)
        layout.addWidget(QLabel("Nem (%):"), 5, 0)
        layout.addWidget(QLabel("Enlem:"), 6, 0)
        layout.addWidget(QLabel("Boylam:"), 7, 0)

        paket = QLineEdit()
        paket.setReadOnly(True)
        paket.setObjectName("paket")
        layout.addWidget(paket, 1, 1)

        ivme = QLineEdit()
        ivme.setReadOnly(True)
        ivme.setObjectName("ivme")
        layout.addWidget(ivme, 2, 1)

        irtifa = QLineEdit()
        irtifa.setReadOnly(True)
        irtifa.setObjectName("irtifa")
        layout.addWidget(irtifa, 3, 1)

        sicaklik = QLineEdit()
        sicaklik.setReadOnly(True)
        sicaklik.setObjectName("sicaklik")
        layout.addWidget(sicaklik, 4, 1)

        nem = QLineEdit()
        nem.setReadOnly(True)
        nem.setObjectName("nem")
        layout.addWidget(nem, 5, 1)

        enlem = QLineEdit()
        enlem.setReadOnly(True)
        enlem.setObjectName("enlem")
        layout.addWidget(enlem, 6, 1)

        boylam = QLineEdit()
        boylam.setReadOnly(True)
        boylam.setObjectName("boylam")
        layout.addWidget(boylam, 7, 1)

        return frame

    def create_roket_widget(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QVBoxLayout(frame)

        label = QLabel("ROKET")
        label.setStyleSheet("font-weight: bold")
        layout.addWidget(label)

        status_label = QLabel()
        status_label.setObjectName("status")
        layout.addWidget(status_label)

        return frame

    def create_pil_widget(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QVBoxLayout(frame)

        label = QLabel("PİL")
        label.setStyleSheet("font-weight: bold")
        layout.addWidget(label)

        # Battery charge indicator
        charge_layout = QHBoxLayout()
        charge_layout.addWidget(QLabel("Şarj Durumu:"))
        self.charge_label = QLabel("100%")
        self.charge_label.setObjectName("charge")
        charge_layout.addWidget(self.charge_label)
        layout.addLayout(charge_layout)

        # Battery temperature indicator
        temperature_layout = QHBoxLayout()
        temperature_layout.addWidget(QLabel("Sıcaklık:"))
        self.temperature_label = QLabel("25°C")
        self.temperature_label.setObjectName("temperature")
        temperature_layout.addWidget(self.temperature_label)
        layout.addLayout(temperature_layout)

        # Battery voltage indicator
        voltage_layout = QHBoxLayout()
        voltage_layout.addWidget(QLabel("Gerilim:"))
        self.voltage_label = QLabel("12V")
        self.voltage_label.setObjectName("voltage")
        voltage_layout.addWidget(self.voltage_label)
        layout.addLayout(voltage_layout)

        return frame

    def update_values(self):
        # Update system values with random values
        self.widget1.findChild(QLineEdit, "paket").setText(f"{random.randint(1, 100)}")
        self.widget1.findChild(QLineEdit, "ivme").setText(f"{random.uniform(1, 10):.2f}")
        self.widget1.findChild(QLineEdit, "irtifa").setText(f"{random.randint(1, 1000)}")
        self.widget1.findChild(QLineEdit, "sicaklik").setText(f"{random.randint(-50, 50)}°C")
        self.widget1.findChild(QLineEdit, "nem").setText(f"{random.randint(0, 100)}%")
        self.widget1.findChild(QLineEdit, "enlem").setText(f"{random.uniform(-90, 90):.6f}")
        self.widget1.findChild(QLineEdit, "boylam").setText(f"{random.uniform(-180, 180):.6f}")

        self.widget2.findChild(QLineEdit, "paket").setText(f"{random.randint(1, 100)}")
        self.widget2.findChild(QLineEdit, "ivme").setText(f"{random.uniform(1, 10):.2f}")
        self.widget2.findChild(QLineEdit, "irtifa").setText(f"{random.randint(1, 1000)}")
        self.widget2.findChild(QLineEdit, "sicaklik").setText(f"{random.randint(-50, 50)}°C")
        self.widget2.findChild(QLineEdit, "nem").setText(f"{random.randint(0, 100)}%")
        self.widget2.findChild(QLineEdit, "enlem").setText(f"{random.uniform(-90, 90):.6f}")
        self.widget2.findChild(QLineEdit, "boylam").setText(f"{random.uniform(-180, 180):.6f}")

        self.widget3.findChild(QLineEdit, "paket").setText(f"{random.randint(1, 100)}")
        self.widget3.findChild(QLineEdit, "ivme").setText(f"{random.uniform(1, 10):.2f}")
        self.widget3.findChild(QLineEdit, "irtifa").setText(f"{random.randint(1, 1000)}")
        self.widget3.findChild(QLineEdit, "sicaklik").setText(f"{random.randint(-50, 50)}°C")
        self.widget3.findChild(QLineEdit, "nem").setText(f"{random.randint(0, 100)}%")
        self.widget3.findChild(QLineEdit, "enlem").setText(f"{random.uniform(-90, 90):.6f}")
        self.widget3.findChild(QLineEdit, "boylam").setText(f"{random.uniform(-180, 180):.6f}")        

    def start_simulation(self):
        # Start updating system values every second
        self.timer.start(1000)

    def stop_simulation(self):
        # Stop updating system values
        self.timer.stop()

        self.widget3.findChild(QLabel, "charge").setText(f"{random.randint(0, 100)}%")
        self.widget3.findChild(QLabel, "temperature").setText(f"{random.uniform(20, 50):.1f}°C")
        self.widget3.findChild(QLabel, "voltage").setText(f"{random.uniform(10, 14):.1f}V")

    def start_simulation(self):
        # Start simulation timer
        self.timer.start(1000)

    def stop_simulation(self):
        # Stop simulation timer
        self.timer.stop()

    def toggle_simulation(self):
        # Toggle simulation timer
        if self.timer.isActive():
            self.stop_simulation()
            self.start_button.setText("Başlat")
            self.status_label.setText("Simülasyon durduruldu.")
        else:
            self.start_simulation()
            self.start_button.setText("Durdur")
            self.status_label.setText("Simülasyon başlatıldı.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

