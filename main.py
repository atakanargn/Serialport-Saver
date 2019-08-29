from serial import Serial
from random import randint
from time import sleep
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from STF_GUI import Ui_MainWindow
import serial.tools.list_ports

class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dosyaAdi = "dosya.txt"
        self.seciliPort = ""
        self.conn = Serial()
        self.comlist = []

        self.timer = QTimer() 
        self.timer.timeout.connect(self.listele)
        self.timer.start(500)

        self.arduinoTimer = QTimer()
        self.arduinoTimer.timeout.connect(self.cekYaz)

    def baglan(self):
        from serial import Serial
        self.conn.baudrate=9600
        try:
            self.conn.close()
        except:
            pass
        self.conn.setPort(self.seciliPort)
        sleep(1)
        self.conn.open()
        self.conn.close()
        sleep(1)
        self.conn.open()
        # delay(20)
        self.arduinoTimer.start(20)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
    
    def durdur(self):
        from serial import Serial
        self.conn.baudrate=9600
        try:
            self.conn.close()
        except:
            pass

        self.arduinoTimer.stop()
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)

    def getText(self,seciliPort):
        self.seciliPort = seciliPort
    
    def getDosyaAdi(self, gelen):
        self.dosyaAdi = gelen

    def listele(self):
        self.comlist = serial.tools.list_ports.comports()
        portListe = []
        for port in self.comlist:
            portListe.append(str(port).split(" ")[0])
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(portListe)
    
    def cekYaz(self):
        gelen = self.conn.readline().decode("utf8") #("\r\n{},{}").format(randint(25,30),randint(50,60))
        dosya = open(self.dosyaAdi,"a+")
        dosya.write(gelen)
        dosya.close()
        # Arduino : delay(20)

if __name__ == '__main__':
    while 1:
        app = QApplication([])
        pencere = Pencere()
        pencere.show()
        app.exec_()