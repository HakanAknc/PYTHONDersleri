#Bu arayuz üzerind çalışşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşş
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QLabel, QTabWidget, QHBoxLayout
from YeniArayuz04 import MainWindow
from YeniArayuz05 import SerialSenderWidget    # önemliiiiiiiiiiiiiiii
from YeniArayuz06 import SerialPortWidget

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Bozdoğan Roket Yer İstasyonu")

# Create a tab widget
tab_widget = QTabWidget()

# First tab
first_tab = QWidget()
first_tab_layout = QVBoxLayout()
first_tab_layout.addWidget(SerialSenderWidget())
first_tab_layout.addWidget(SerialPortWidget())
#first_tab.setStyleSheet("background-color: #ddd")
first_tab.setLayout(first_tab_layout)
tab_widget.addTab(first_tab, "Port Seç")


# Second tab
second_tab = QWidget()
second_tab_layout = QHBoxLayout()

# Create a main splitter
main_splitter = QSplitter(Qt.Vertical)
#main_splitter.setSizes([1000, 1000])

# Create a central widget
central_widget = QWidget()

# Create a horizontal layout
h1_layout = QVBoxLayout()
h2_layout = QVBoxLayout()

# Create a vertical layout
v1_layout = QHBoxLayout()
v2_layout = QHBoxLayout()



# First widget
first_widget = QWidget()
first_widget.setMaximumWidth(int(window.width()))
first_widget.setMaximumHeight(int(window.height()))
#first_widget.setFixedSize(300, 300)
first_widget.setStyleSheet("background-color: #ddd")
first_widget_layout = QVBoxLayout()

first_widget_layout.addWidget(MainWindow())

first_widget.setLayout(first_widget_layout)

# Second widget
second_widget = QWidget()
second_widget.setMaximumWidth(int(window.width()))
second_widget.setMaximumHeight(int(window.height()))
#second_widget.setFixedSize(300, 300)
second_widget.setStyleSheet("background-color: #ddd")
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

#Add widgets to the first horizontal layout
h1_layout.addWidget(first_widget)
h1_layout.addWidget(second_widget)

#Add widgets to the second horizontal layout
h2_layout.addWidget(third_widget)

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

# Fourth widget
fourth_widget = QWidget()
fourth_widget.setMaximumWidth(int(window.width()))
fourth_widget.setMaximumHeight(int(window.height()))
fourth_widget.setStyleSheet("background-color: #ddd")
fourth_widget_layout = QVBoxLayout()
label4 = QLabel("Burda harita olucak")
label4.setAlignment(Qt.AlignCenter)
fourth_widget_layout.addWidget(label4)
fourth_widget.setLayout(fourth_widget_layout)

# Add widgets to the first horizontal layout
h1_layout.addWidget(first_widget)
h1_layout.addWidget(second_widget)

# Add widgets to the second horizontal layout
h2_layout.addWidget(third_widget)
h2_layout.addWidget(fourth_widget)

# Add the first and second horizontal layouts to the vertical layout
v1_layout.addLayout(h1_layout)
v1_layout.addLayout(h2_layout)

# Set the layout to the central widget
central_widget.setLayout(v1_layout)

# Add the central widget to the main splitter
main_splitter.addWidget(central_widget)

# Add splitter to second tab layout
second_tab_layout.addWidget(main_splitter)
second_tab.setLayout(second_tab_layout)

# third tab
third_tab = QWidget()
third_tab_layout = QVBoxLayout()
label = QLabel("Bozdoğan Roket")
third_tab_layout.addWidget(label)
third_tab.setLayout(third_tab_layout)
tab_widget.addTab(third_tab, "Roket")

#Set tab widget as central widget
window.setCentralWidget(tab_widget)

#Show the main window
window.show()

#Timer to update the labels
timer = QTimer()
timer.start(1000)

#Function to update the labels


#Run the application
sys.exit(app.exec_())