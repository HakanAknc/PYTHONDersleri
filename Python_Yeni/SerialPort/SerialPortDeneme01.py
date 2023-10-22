import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *

class SerialPortWidget(QWidget):
    def __init__(self):
        super().__init__()

        # seri port bağlantısı oluşturma
        self.serial_port = QSerialPort('COM3')
        self.serial_port.setBaudRate(QSerialPort.Baud9600)
        self.serial_port.readyRead.connect(self.receive_data)

        # arayüz öğeleri
        self.text_edit = QTextEdit()
        self.open_button = QPushButton('Bağlan')
        self.open_button.clicked.connect(self.open_port)
        self.close_button = QPushButton('Bağlantıyı Kes')
        self.close_button.clicked.connect(self.close_port)

        # arayüz düzeni
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.open_button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

    def open_port(self):
        # seri port bağlantısını açma
        if not self.serial_port.isOpen():
            if self.serial_port.open(QIODevice.ReadWrite):
                self.text_edit.append('Bağlantı açıldı')

    def close_port(self):
        # seri port bağlantısını kapatma
        if self.serial_port.isOpen():
            self.serial_port.close()
            self.text_edit.append('Bağlantı kapatıldı')

    def receive_data(self):
        # seri porttan gelen verileri okuma
        while self.serial_port.canReadLine():
            data = self.serial_port.readLine().data().decode()
            self.text_edit.append(data.strip())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialPortWidget()
    widget.show()
    sys.exit(app.exec_())