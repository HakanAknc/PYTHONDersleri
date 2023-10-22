import sys
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, \
    QComboBox, QLineEdit


class SerialSenderWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Arayüz öğeleri
        self.port_list_label = QLabel('Açık Portlar:')
        self.port_list_widget = QComboBox()
        self.refresh_button = QPushButton('Yenile')
        self.baudrate_label = QLabel('Baudrate:')
        self.baudrate_widget = QComboBox()
        self.baudrate_widget.addItems(['9600', '19200', '38400', '57600', '115200']) # Default values
        self.send_label = QLabel('Gönderilecek Veri:')
        self.send_text = QLineEdit()
        self.send_button = QPushButton('Gönder Gelsinnn')

        # Arayüz düzeni
        layout = QVBoxLayout()
        port_layout = QHBoxLayout()
        port_layout.addWidget(self.port_list_label)
        port_layout.addWidget(self.port_list_widget)
        port_layout.addWidget(self.refresh_button)
        layout.addLayout(port_layout)
        baudrate_layout = QHBoxLayout()
        baudrate_layout.addWidget(self.baudrate_label)
        baudrate_layout.addWidget(self.baudrate_widget)
        layout.addLayout(baudrate_layout)
        layout.addWidget(self.send_label)
        layout.addWidget(self.send_text)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        # Olayları bağlama
        self.send_button.clicked.connect(self.send_data)
        self.refresh_button.clicked.connect(self.refresh_ports)

        # Açık portları listeleme
        self.refresh_ports()

    def refresh_ports(self):
        self.port_list_widget.clear()
        ports = serial.tools.list_ports.comports()
        for info in ports:
            self.port_list_widget.addItem(info.device)

    def send_data(self):
        # Seçilen portu ve baudrate'i açma
        selected_port = self.port_list_widget.currentText()
        baudrate = int(self.baudrate_widget.currentText())
        with serial.Serial(selected_port, baudrate=baudrate) as serial_port:
            # Veriyi yazdır
            data = self.send_text.text().encode()
            serial_port.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialSenderWidget()
    widget.show()
    sys.exit(app.exec_())