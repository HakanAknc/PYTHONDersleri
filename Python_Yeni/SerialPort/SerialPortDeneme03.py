# Deneme03 sonuca az kaldı
import sys
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QComboBox


class SerialPortWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Arayüz öğeleri
        self.port_list_label = QLabel('Açık Portlar:')
        self.port_list_widget = QComboBox()
        self.refresh_button = QPushButton('Yenile')
        self.connect_button = QPushButton('Bağlan')
        self.disconnect_button = QPushButton('Bağlantıyı Kes')
        self.receive_label = QLabel('Alınan Veri:')
        self.receive_text = QLabel()

        # Arayüz düzeni
        layout = QVBoxLayout()
        layout.addWidget(self.port_list_label)
        layout.addWidget(self.port_list_widget)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.receive_label)
        layout.addWidget(self.receive_text)
        self.setLayout(layout)

        # Olayları bağlama
        self.refresh_button.clicked.connect(self.refresh_ports)
        self.connect_button.clicked.connect(self.open_port)
        self.disconnect_button.clicked.connect(self.close_port)
        self.serial_port = None

        # Açık portları listeleme
        self.refresh_ports()

    def refresh_ports(self):
        self.port_list_widget.clear()
        ports = serial.tools.list_ports.comports()
        for info in ports:
            self.port_list_widget.addItem(info.device)

    def open_port(self):
        # Seçilen portu açma
        selected_port = self.port_list_widget.currentText()
        self.serial_port = serial.Serial(selected_port, baudrate=9600)
        if self.serial_port.is_open:
            self.receive_text.setText('Bağlantı açıldı')

    def close_port(self):
        # Portu kapatma
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.receive_text.setText('Bağlantı kapatıldı')

    def receive_data(self):
        # Seri porttan gelen verileri okuma
        if self.serial_port and self.serial_port.is_open and self.serial_port.in_waiting:
            data = self.serial_port.readline().decode().strip()
            self.receive_text.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialPortWidget()
    widget.show()
    sys.exit(app.exec_())