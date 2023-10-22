# pip install pyserial---->indirdiğimiz kütüphane
def veribasma():
 
 paket=packet[0]
 print("paket:"+paket)
 takimid=packet[1]
 print("takım id:"+takimid)
 irtifa=packet[2]
 print("irtifa:"+irtifa)
 ivmex=packet[3]
 print("ivme:"+ivmex)
 ivmey=packet[4]
 print("ivmey:"+ivmey)
 ivmez=packet[5]
 print("ivmez:"+ivmez)
 jiroskopx=packet[6]
 print("jiroscopx:"+jiroskopx)
 jiroskopy=packet[7]
 print("jiroskopy:"+ jiroskopy)
 jiroskopz=packet[8]
 print("jiroskopz:" +jiroskopz)
 enlem=packet[9]
 print("enlem:"+enlem)
 boylam=packet[10]
 print("boylam:"+boylam)
 gpsirtifa=packet[11]
 print("gps irtifa:"+gpsirtifa)
 parasutdurum=packet[12]
 print("paraşüt durum:"+parasutdurum)
 pilsicaklik=packet[13]
 print("pil sıcaklık:"+pilsicaklik)
 pilyuzdesi=packet[14]
 print("pil yüzdedesi"+pilyuzdesi)
 roketsaat=packet[15]
 print("roket saat:"+roketsaat)
 roketdakika=packet[16]
 print("roket dakika:"+roketdakika)
 roketsaniye=packet[17]
 print("roket saniye:"+roketsaniye)

 print("***************************************  Yenilendi *******************************")

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        packet=packet.decode('utf')
        packet=packet.split(".")
        veribasma()




