import sys
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort


class SerialPortWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Arayüz öğeleri
        self.port_list_label = QLabel('Açık Portlar:')
        self.port_list_widget = QListWidget()
        self.connect_button = QPushButton('Bağlan')
        self.disconnect_button = QPushButton('Bağlantıyı Kes')
        self.receive_label = QLabel('Alınan Veri:')
        self.receive_text = QLabel()

        # Arayüz düzeni
        layout = QVBoxLayout()
        layout.addWidget(self.port_list_label)
        layout.addWidget(self.port_list_widget)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.receive_label)
        layout.addWidget(self.receive_text)
        self.setLayout(layout)

        # Olayları bağlama
        self.connect_button.clicked.connect(self.open_port)
        self.disconnect_button.clicked.connect(self.close_port)
        self.serial_port = QSerialPort()
        self.serial_port.readyRead.connect(self.receive_data)

        # Açık portları listeleme
        for info in QSerialPortInfo.availablePorts():
            self.port_list_widget.addItem(info.portName())

    def open_port(self):
        # Seçilen portu açma
        selected_port = self.port_list_widget.currentItem().text()
        self.serial_port.setPortName(selected_port)
        self.serial_port.setBaudRate(QSerialPort.Baud9600)
        if not self.serial_port.isOpen():
            if self.serial_port.open(QIODevice.ReadWrite):
                self.receive_text.setText('Bağlantı açıldı')

    def close_port(self):
        # Portu kapatma
        if self.serial_port.isOpen():
            self.serial_port.close()
            self.receive_text.setText('Bağlantı kapatıldı')

    def receive_data(self):
        # Seri porttan gelen verileri okuma
        while self.serial_port.canReadLine():
            data = self.serial_port.readLine().data().decode()
            self.receive_text.setText(data.strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialPortWidget()
    widget.show()
    sys.exit(app.exec_())