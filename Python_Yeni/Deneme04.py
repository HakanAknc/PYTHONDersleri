import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 ile Roket Arayüzü'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a tab widget
        tabs = QTabWidget(self)

        # Create tabs
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        tab5 = QWidget()

        # Add tabs to tab widget
        tabs.addTab(tab1, "Port")
        tabs.addTab(tab2, "Anasayfa")
        tabs.addTab(tab3, "Harita")
        tabs.addTab(tab4, "Haberleşme")
        tabs.addTab(tab5, "İletişim")

        # Create labels for each tab
        label1 = QLabel("Avyonik ve Yazılım Kaptanı: Usame Salman")
        label2 = QLabel("Yardımcısı: Hakan Akıncı")
        label3 = QLabel("Burda harita olucak")
        label4 = QLabel("Burda haberleşme olucak")
        label5 = QLabel("Burda iletişim olucak")

        # Create layout for each tab
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QVBoxLayout()

        # Add labels to layouts
        layout1.addWidget(label1)
        layout2.addWidget(label2)
        layout3.addWidget(label3)
        layout4.addWidget(label4)
        layout5.addWidget(label5)

        # Set layouts for tabs
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)
        tab3.setLayout(layout3)
        tab4.setLayout(layout4)
        tab5.setLayout(layout5)

        # Add tabs to main window layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())