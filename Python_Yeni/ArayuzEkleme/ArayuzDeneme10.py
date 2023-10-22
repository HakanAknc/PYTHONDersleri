#ArayuzDeneme10 başarılı veri girilmiyor
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QLineEdit, QGridLayout

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

        layout.addWidget(self.create_sistem_widget("ANA SİSTEM:"))
        layout.addWidget(self.create_sistem_widget("YEDEK SİSTEM:"))
        layout.addWidget(self.create_sistem_widget("FAYDALI YÜK:"))

    def create_sistem_widget(self, sistem_adi):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QGridLayout(frame)

        label = QLabel(sistem_adi)
        label.setStyleSheet("font-weight: bold")

        layout.addWidget(label, 0, 0)

        lineEdit1 = QLineEdit()
        lineEdit1.setReadOnly(True)
        layout.addWidget(QLabel("Paket (m):"), 1, 0)
        layout.addWidget(lineEdit1, 1, 1)

        lineEdit2 = QLineEdit()
        lineEdit2.setReadOnly(True)
        layout.addWidget(QLabel("Takım ID:"), 2, 0)
        layout.addWidget(lineEdit2, 2, 1)

        lineEdit3 = QLineEdit()
        lineEdit3.setReadOnly(True)
        layout.addWidget(QLabel("İrtifa (m):"), 3, 0)
        layout.addWidget(lineEdit3, 3, 1)

        lineEdit4 = QLineEdit()
        lineEdit4.setReadOnly(True)
        layout.addWidget(QLabel("İvme (m/s²):"), 4, 0)
        layout.addWidget(lineEdit4, 4, 1)

        return frame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())