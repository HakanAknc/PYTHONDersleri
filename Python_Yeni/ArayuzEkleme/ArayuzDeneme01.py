#Arayuzun ilk hali
import sys
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QLabel, QTabWidget, QHBoxLayout

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Bozdoğan Roket Yer İstasyonu V13")

# Create a tab widget
tab_widget = QTabWidget()

# First tab
first_tab = QWidget()
first_tab_layout = QVBoxLayout()
label = QLabel("Bozdoğan Roket")
first_tab_layout.addWidget(label)
first_tab.setLayout(first_tab_layout)
tab_widget.addTab(first_tab, "Port Seç")

# Second tab
second_tab = QWidget()
second_tab_layout = QVBoxLayout()

# Create a main splitter
main_splitter = QSplitter(Qt.Horizontal)
#main_splitter.setSizes([1000, 1000])

# Create a central widget
central_widget = QWidget()

# Create a horizontal layout
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()

# Create a vertical layout
v1_layout = QVBoxLayout()
v2_layout = QVBoxLayout()

# First widget
first_widget = QWidget()
first_widget.setMaximumWidth(int(window.width()))
first_widget.setMaximumHeight(int(window.height()))
#first_widget.setFixedSize(300, 300)
first_widget.setStyleSheet("background-color: #ddd")
first_widget_layout = QVBoxLayout()
label1 = QLabel(f"Takım ID: {1234}")
label2 = QLabel(f"Sistem Numarası:2")
paketno_label = QLabel("0")
irtifa_label = QLabel("0")
label5 = QLabel(f"İvme:5.4")
first_widget_layout.addWidget(label1)
first_widget_layout.addWidget(label2)
first_widget_layout.addWidget(paketno_label)
first_widget_layout.addWidget(irtifa_label)
first_widget_layout.addWidget(label5)
first_widget.setLayout(first_widget_layout)

# Second widget
second_widget = QWidget()
second_widget.setMaximumWidth(int(window.width()))
second_widget.setMaximumHeight(int(window.height()))
#second_widget.setFixedSize(300, 300)
second_widget.setStyleSheet("background-color: #fff")
second_widget_layout = QVBoxLayout()
for i in range(10):
    label = QLabel(f"Label {i+1}")
    second_widget_layout.addWidget(label)

second_widget.setLayout(second_widget_layout)

#Third widget
third_widget = QTabWidget()
third_widget.setMaximumWidth(int(window.width()))
third_widget.setMaximumHeight(int(window.height()))
#third_widget.setFixedSize(300, 300)
tab1 = QWidget()
tab1.setStyleSheet("background-color: #eee")
tab1_layout = QVBoxLayout()
for i in range(5):
    label = QLabel(f"Tab 1 Label {i+1}")
    tab1_layout.addWidget(label)
tab1.setLayout(tab1_layout)

tab2 = QWidget()
tab2.setStyleSheet("background-color: #550077")
tab2_layout = QVBoxLayout()
for i in range(7):
    label = QLabel(f"Tab 2 Label {i+1}")
    tab2_layout.addWidget(label)
tab2.setLayout(tab2_layout)

third_widget.addTab(tab1, "Konum Grafiği")
third_widget.addTab(tab2, "Hız Grafiği")


#Fourth widget
fourth_widget = QWebEngineView()
fourth_widget.setMaximumWidth(int(window.width()))
fourth_widget.setMaximumHeight(int(window.height()))
#fourth_widget.setFixedSize(300, 300)
fourth_widget.load(QUrl("https://www.google.com/maps/@37.8724885,32.4928685,17.5z"))


#Add widgets to the first horizontal layout
h1_layout.addWidget(first_widget)
h1_layout.addWidget(second_widget)

#Add widgets to the second horizontal layout
h2_layout.addWidget(third_widget)
h2_layout.addWidget(fourth_widget)

#Add the first and second horizontal layouts to the vertical layout
v1_layout.addLayout(h1_layout)
v1_layout.addLayout(h2_layout)

#Set the layout to the central widget
central_widget.setLayout(v1_layout)

#Add the central widget to the main splitter
main_splitter.addWidget(central_widget)

#Add splitter to second tab layout
second_tab_layout.addWidget(main_splitter)
second_tab.setLayout(second_tab_layout)

#Add second tab to tab widget
tab_widget.addTab(second_tab, "Anasayfa")

# third tab

third_tab = QWidget()
third_tab_layout = QVBoxLayout()
label = QLabel("Bozdoğan Roket")
third_tab_layout.addWidget(label)
third_tab.setLayout(third_tab_layout)
tab_widget.addTab(third_tab, "İletişim")

#Set tab widget as central widget
window.setCentralWidget(tab_widget)

#Show the main window
window.show()

#Timer to update the labels
timer = QTimer()
timer.timeout.connect(lambda: update_labels(paketno_label, irtifa_label))
timer.start(1000)

#Function to update the labels
def update_labels(paketno_label, irtifa_label):
    first_value = int(paketno_label.text()) + 1
    second_value = float(irtifa_label.text()) + 5
    paketno_label.setText(str(first_value))
    irtifa_label.setText(str(second_value))
    if first_value == 100:
        timer.stop()

#Run the application
sys.exit(app.exec_())