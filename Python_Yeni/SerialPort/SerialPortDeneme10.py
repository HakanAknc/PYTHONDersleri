#Deneme10 veri alınıyor utf-8 eklendi 
import sys
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
)


class SerialPortWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Interface elements
        self.port_list_label = QLabel('Açık Portlar:')
        self.port_list_widget = QComboBox()
        self.baudrate_label = QLabel('Baudrate:')
        self.baudrate_edit = QLineEdit('9600')
        self.refresh_button = QPushButton('Yenile')
        self.connect_button = QPushButton('Bağlan')
        self.disconnect_button = QPushButton('Bağlantıyı Kes')
        self.receive_label = QLabel('Alınan Veri:')
        self.receive_text = QLabel()

        # Interface layout
        layout = QVBoxLayout()
        port_layout = QHBoxLayout()
        port_layout.addWidget(self.port_list_label)
        port_layout.addWidget(self.port_list_widget)
        layout.addLayout(port_layout)
        baud_layout = QHBoxLayout()
        baud_layout.addWidget(self.baudrate_label)
        baud_layout.addWidget(self.baudrate_edit)
        layout.addLayout(baud_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.receive_label)
        layout.addWidget(self.receive_text)
        self.setLayout(layout)

        # Connect events
        self.refresh_button.clicked.connect(self.refresh_ports)
        self.connect_button.clicked.connect(self.open_port)
        self.disconnect_button.clicked.connect(self.close_port)
        self.serial_port = None

        # List available ports
        self.refresh_ports()

    def refresh_ports(self):
        self.port_list_widget.clear()
        ports = serial.tools.list_ports.comports()
        for info in ports:
            self.port_list_widget.addItem(info.device)

    def open_port(self):
        # Open selected port with the chosen baud rate
        selected_port = self.port_list_widget.currentText()
        baudrate = int(self.baudrate_edit.text())
        self.serial_port = serial.Serial(selected_port, baudrate=baudrate)
        if self.serial_port.is_open:
            self.receive_text.setText('Bağlantı açıldı')
            # Start reading from serial port
            self.serial_port.flushInput()
            self.serial_port.timeout = 0.1
            self.timer = QTimer()
            self.timer.timeout.connect(self.receive_data)
            self.timer.start()

    def close_port(self):
        # Close serial port
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.receive_text.setText('Bağlantı kapatıldı')

    def receive_data(self):
        # Read data from serial port
        if self.serial_port and self.serial_port.is_open and self.serial_port.in_waiting:
            data = self.serial_port.readline().decode('utf-8').strip()
            self.receive_text.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialPortWidget()
    widget.show()
    sys.exit(app.exec_())