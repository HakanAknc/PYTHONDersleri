#ArayuzDeneme12 başarılı veri alınıyor
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QLineEdit, QGridLayout
from PyQt5.QtCore import QTimer

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

        layout.setSpacing(10)  #birbirinden ayırıyor

        self.widget1 = self.create_sistem_widget("ANA SİSTEM:")   #widget isimleri
        self.widget2 = self.create_sistem_widget("YEDEK SİSTEM:")
        self.widget3 = self.create_sistem_widget("FAYDALI YÜK:")

        layout.addWidget(self.widget1)   #widget numaraları
        layout.addWidget(self.widget2) 
        layout.addWidget(self.widget3)

        # Set up timer to update values every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(1000)   #verilen değişme hızı

    def create_sistem_widget(self, sistem_adi):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QGridLayout(frame)

        label = QLabel(sistem_adi)
        label.setStyleSheet("font-weight: bold") #yazı tipini değiştiriyor

        layout.addWidget(label, 0, 0) # widgetlerin içindekilerinin konumunu değiştiriyor

        ana_paket = QLineEdit()
        ana_paket.setReadOnly(True)  #değer girmemize izin veriyor
        ana_paket.setObjectName("paket")
        layout.addWidget(QLabel("Paket:"), 1, 0) #konum değiştiriyor
        layout.addWidget(ana_paket, 1, 1)

        ana_takim_id = QLineEdit()
        ana_takim_id.setReadOnly(True)
        ana_takim_id.setObjectName("takimid")
        layout.addWidget(QLabel("Takım ID:"), 2, 0)
        layout.addWidget(ana_takim_id, 2, 1)

        ana_irtifa = QLineEdit()
        ana_irtifa.setReadOnly(True)
        ana_irtifa.setObjectName("irtifa")
        layout.addWidget(QLabel("İrtifa:"), 3, 0)
        layout.addWidget(ana_irtifa, 3, 1)

        ana_ivme = QLineEdit()
        ana_ivme.setReadOnly(True)
        ana_ivme.setObjectName("ivme")
        layout.addWidget(QLabel("İvme:"), 4, 0)
        layout.addWidget(ana_ivme, 4, 1)

        ana_eğim = QLineEdit()
        ana_eğim.setReadOnly(True)
        ana_eğim.setObjectName("eğim")
        layout.addWidget(QLabel("Eğim:"), 5, 0)
        layout.addWidget(ana_eğim, 5, 1)

        ana_sicaklik = QLineEdit()
        ana_sicaklik.setReadOnly(True)
        ana_sicaklik.setObjectName("sicaklik")
        layout.addWidget(QLabel("Sıcaklık:"), 6, 0)
        layout.addWidget(ana_sicaklik, 6, 1)

        ana_enlem = QLineEdit()
        ana_enlem.setReadOnly(True)
        ana_enlem.setObjectName("enlem")
        layout.addWidget(QLabel("Enlem:"), 7, 0)
        layout.addWidget(ana_enlem, 7, 1)

        ana_boylam = QLineEdit()
        ana_boylam.setReadOnly(True)
        ana_boylam.setObjectName("boylam")
        layout.addWidget(QLabel("Boylam:"), 8, 0)
        layout.addWidget(ana_boylam, 8, 1)

        ana_atesleme_durumu = QLineEdit()
        ana_atesleme_durumu.setReadOnly(True)
        ana_atesleme_durumu.setObjectName("ateslemedurumu")
        layout.addWidget(QLabel("Ateşleme Durumu:"), 9, 0)
        layout.addWidget(ana_atesleme_durumu, 9, 1)

        ana_saat = QLineEdit()
        ana_saat.setReadOnly(True)
        ana_saat.setObjectName("saat")
        layout.addWidget(QLabel("Saat:"), 10, 0)
        layout.addWidget(ana_saat, 10, 1)

        ana_pil_sicaklik = QLineEdit()
        ana_pil_sicaklik.setReadOnly(True)
        ana_pil_sicaklik.setObjectName("pilsicaklik")
        layout.addWidget(QLabel("Pil Sıcaklık:"), 11, 0)
        layout.addWidget(ana_pil_sicaklik, 11, 1)

        ana_pil_yüzdesi = QLineEdit()
        ana_pil_yüzdesi.setReadOnly(True)
        ana_pil_yüzdesi.setObjectName("pilyüzdesi")
        layout.addWidget(QLabel("Pil Yüzdesi:"), 12, 0)
        layout.addWidget(ana_pil_yüzdesi, 12, 1)

        ana_nem = QLineEdit()
        ana_nem.setReadOnly(True)
        ana_nem.setObjectName("nem")
        layout.addWidget(QLabel("Nem:"), 13, 0)
        layout.addWidget(ana_nem, 13, 1)

        frame.setLayout(layout)

        return frame

    def update_values(self):
        # Generate random values for each parameter
        ana_sistem_paket = round(random.uniform(0, 10), 2)
        ana_sistem_ivme = round(random.uniform(0, 5), 2)
        ana_sistem_irtifa = round(random.uniform(0, 500), 2)
        ana_sistem_sicaklik = round(random.uniform(-50, 50), 2)
        ana_sistem_nem = round(random.uniform(0, 100), 2)
        ana_sistem_eğim = round(random.uniform(10, 50), 2)
        ana_sistem_enlem = round(random.uniform(10, 50), 2)
        ana_sistem_boylam = round(random.uniform(10, 100), 2)
        ana_sistem_takim_id = round(random.uniform(10, 100), 2)
        ana_sistem_atesleme_durumu = round(random.uniform(10, 100), 2)
        ana_sistem_saat = round(random.uniform(10, 100), 2)
        ana_sistem_pil_sicaklik = round(random.uniform(10, 100), 2)
        ana_sistem_pil_yüzdesi = round(random.uniform(10, 100), 2)


        yedek_sistem_paket = round(random.uniform(0, 10), 2)
        yedek_sistem_ivme = round(random.uniform(0, 5), 2)
        yedek_sistem_irtifa = round(random.uniform(0, 500), 2)
        yedek_sistem_sicaklik = round(random.uniform(-50, 50), 2)
        yedek_sistem_nem = round(random.uniform(0, 100), 2)
        yedek_sistem_eğim = round(random.uniform(10, 50), 2)
        yedek_sistem_enlem = round(random.uniform(10, 50), 2)
        yedek_sistem_boylam = round(random.uniform(10, 100), 2)
        yedek_sistem_takim_id = round(random.uniform(10, 100), 2)
        yedek_sistem_atesleme_durumu = round(random.uniform(10, 100), 2)
        yedek_sistem_saat = round(random.uniform(10, 100), 2)
        yedek_sistem_pil_sicaklik = round(random.uniform(10, 100), 2)
        yedek_sistem_pil_yüzdesi = round(random.uniform(10, 100), 2)


        faydali_yuk_paket = round(random.uniform(0, 10), 2)
        faydali_yuk_ivme = round(random.uniform(0, 5), 2)
        faydali_yuk_irtifa = round(random.uniform(0, 500), 2)
        faydali_yuk_sicaklik = round(random.uniform(-50, 50), 2)
        faydali_yuk_nem = round(random.uniform(0, 100), 2)
        faydali_yük_eğim = round(random.uniform(10, 50), 2)
        faydali_yük_enlem = round(random.uniform(10, 50), 2)
        faydali_yük_boylam = round(random.uniform(10, 100), 2)
        faydali_yük_takim_id = round(random.uniform(10, 100), 2)
        faydali_yük_atesleme_durumu = round(random.uniform(10, 100), 2)
        faydali_yük_saat = round(random.uniform(10, 100), 2)
        faydali_yük_pil_sicaklik = round(random.uniform(10, 100), 2)
        faydali_yük_pil_yüzdesi = round(random.uniform(10, 100), 2)


        # Update the values in the UI
        self.widget1.findChild(QLineEdit, "paket").setText(str(ana_sistem_paket))
        self.widget1.findChild(QLineEdit, "ivme").setText(str(ana_sistem_ivme))
        self.widget1.findChild(QLineEdit, "irtifa").setText(str(ana_sistem_irtifa))
        self.widget1.findChild(QLineEdit, "sicaklik").setText(str(ana_sistem_sicaklik))
        self.widget1.findChild(QLineEdit, "nem").setText(str(ana_sistem_nem))
        self.widget1.findChild(QLineEdit, "eğim").setText(str(ana_sistem_eğim))
        self.widget1.findChild(QLineEdit, "enlem").setText(str(ana_sistem_enlem))
        self.widget1.findChild(QLineEdit, "boylam").setText(str(ana_sistem_boylam))
        self.widget1.findChild(QLineEdit, "takimid").setText(str(ana_sistem_takim_id))
        self.widget1.findChild(QLineEdit, "ateslemedurumu").setText(str(ana_sistem_atesleme_durumu))
        self.widget1.findChild(QLineEdit, "saat").setText(str(ana_sistem_saat))
        self.widget1.findChild(QLineEdit, "pilsicaklik").setText(str(ana_sistem_pil_sicaklik))
        self.widget1.findChild(QLineEdit, "pilyüzdesi").setText(str(ana_sistem_pil_yüzdesi))


        self.widget2.findChild(QLineEdit, "paket").setText(str(yedek_sistem_paket))
        self.widget2.findChild(QLineEdit, "ivme").setText(str(yedek_sistem_ivme))
        self.widget2.findChild(QLineEdit, "irtifa").setText(str(yedek_sistem_irtifa))
        self.widget2.findChild(QLineEdit, "sicaklik").setText(str(yedek_sistem_sicaklik))
        self.widget2.findChild(QLineEdit, "nem").setText(str(yedek_sistem_nem))
        self.widget2.findChild(QLineEdit, "eğim").setText(str(yedek_sistem_eğim))
        self.widget2.findChild(QLineEdit, "enlem").setText(str(yedek_sistem_enlem))
        self.widget2.findChild(QLineEdit, "boylam").setText(str(yedek_sistem_boylam))
        self.widget2.findChild(QLineEdit, "takimid").setText(str(yedek_sistem_takim_id))
        self.widget2.findChild(QLineEdit, "ateslemedurumu").setText(str(yedek_sistem_atesleme_durumu))
        self.widget2.findChild(QLineEdit, "saat").setText(str(yedek_sistem_saat))
        self.widget2.findChild(QLineEdit, "pilsicaklik").setText(str(yedek_sistem_pil_sicaklik))
        self.widget2.findChild(QLineEdit, "pilyüzdesi").setText(str(yedek_sistem_pil_yüzdesi))



        self.widget3.findChild(QLineEdit, "paket").setText(str(faydali_yuk_paket))
        self.widget3.findChild(QLineEdit, "ivme").setText(str(faydali_yuk_ivme))
        self.widget3.findChild(QLineEdit, "irtifa").setText(str(faydali_yuk_irtifa))
        self.widget3.findChild(QLineEdit, "sicaklik").setText(str(faydali_yuk_sicaklik))
        self.widget3.findChild(QLineEdit, "nem").setText(str(faydali_yuk_nem))
        self.widget3.findChild(QLineEdit, "eğim").setText(str(faydali_yük_eğim))
        self.widget3.findChild(QLineEdit, "enlem").setText(str(faydali_yük_enlem))
        self.widget3.findChild(QLineEdit, "boylam").setText(str(faydali_yük_boylam))
        self.widget3.findChild(QLineEdit, "takimid").setText(str(faydali_yük_takim_id))
        self.widget3.findChild(QLineEdit, "ateslemedurumu").setText(str(faydali_yük_atesleme_durumu))
        self.widget3.findChild(QLineEdit, "saat").setText(str(faydali_yük_saat))
        self.widget3.findChild(QLineEdit, "pilsicaklik").setText(str(faydali_yük_pil_sicaklik))
        self.widget3.findChild(QLineEdit, "pilyüzdesi").setText(str(faydali_yük_pil_yüzdesi))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
