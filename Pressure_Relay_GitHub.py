
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtWidgets import QApplication
import RPi.GPIO as GPIO
import Test_rc
import time
import board
import busio
from adafruit_ads1x15.single_ended import ADS1115

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 489)
        MainWindow.setStyleSheet("border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 70, 70, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 70, 70, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 70, 70, 255), stop:1 rgba(255, 255, 255, 255));")
        self.page.setObjectName("page")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_7 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_18.addWidget(self.label_7)
        self.lcdNumber3 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber3.setObjectName("lcdNumber3")
        self.horizontalLayout_18.addWidget(self.lcdNumber3)
        self.lcdNumber1 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber1.setObjectName("lcdNumber1")
        self.horizontalLayout_18.addWidget(self.lcdNumber1)
        self.lcdNumber2 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber2.setObjectName("lcdNumber2")
        self.horizontalLayout_18.addWidget(self.lcdNumber2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_18)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_8 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_17.addWidget(self.label_8)
        self.lcdNumber5 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber5.setObjectName("lcdNumber5")
        self.horizontalLayout_17.addWidget(self.lcdNumber5)
        self.lcdNumber6 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber6.setObjectName("lcdNumber6")
        self.horizontalLayout_17.addWidget(self.lcdNumber6)
        self.lcdNumber4 = QtWidgets.QLCDNumber(self.page)
        self.lcdNumber4.setObjectName("lcdNumber4")
        self.horizontalLayout_17.addWidget(self.lcdNumber4)
        self.horizontalLayout.addLayout(self.horizontalLayout_17)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.relay_home = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.relay_home.setFont(font)
        self.relay_home.setObjectName("relay_home")
        self.horizontalLayout_6.addWidget(self.relay_home)
        self.settings_home = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.settings_home.setFont(font)
        self.settings_home.setObjectName("settings_home")
        self.horizontalLayout_6.addWidget(self.settings_home)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_19.addLayout(self.verticalLayout_8)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.verticalLayout_3.addWidget(self.lcdNumber_7)
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.verticalLayout_3.addWidget(self.lcdNumber_8)
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.verticalLayout_3.addWidget(self.lcdNumber_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.settings_relay = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.settings_relay.setFont(font)
        self.settings_relay.setObjectName("settings_relay")
        self.verticalLayout_5.addWidget(self.settings_relay)
        self.pressure_relay = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pressure_relay.setFont(font)
        self.pressure_relay.setObjectName("pressure_relay")
        self.verticalLayout_5.addWidget(self.pressure_relay)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Off_Button = QtWidgets.QPushButton(self.page_2)
        self.Off_Button.setObjectName("Off_Button")
        self.horizontalLayout_3.addWidget(self.Off_Button)
        self.On_Button = QtWidgets.QPushButton(self.page_2)
        self.On_Button.setObjectName("On_Button")
        self.horizontalLayout_3.addWidget(self.On_Button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setWhatsThis("")
        self.page_3.setAutoFillBackground(False)
        self.page_3.setObjectName("page_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.pressure_setting = QtWidgets.QPushButton(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pressure_setting.setFont(font)
        self.pressure_setting.setObjectName("pressure_setting")
        self.verticalLayout_20.addWidget(self.pressure_setting)
        self.relay_setting = QtWidgets.QPushButton(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.relay_setting.setFont(font)
        self.relay_setting.setObjectName("relay_setting")
        self.verticalLayout_20.addWidget(self.relay_setting)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_18.addWidget(self.stackedWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_18.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/ENTER YOUR IMAGE PATH\"/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">LEFT CHAMBER</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CENTRAL CHAMBER</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">RIGHT CHAMBER</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">PRESSURE</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">FLOW</p></body></html>"))
        self.relay_home.setText(_translate("MainWindow", "RELAY"))
        self.settings_home.setText(_translate("MainWindow", "SETTINGS"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LEFT </p><p align=\"center\">CHAMBER</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CENTRAL </p><p align=\"center\">CHAMBER</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">RIGHT </p><p align=\"center\">CHAMBER</p></body></html>"))
        self.settings_relay.setText(_translate("MainWindow", "Settings"))
        self.pressure_relay.setText(_translate("MainWindow", "PRESSURE/FLOW"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">RELAY CONTROL</p></body></html>"))
        self.Off_Button.setText(_translate("MainWindow", "OFF"))
        self.On_Button.setText(_translate("MainWindow", "ON"))
        self.pressure_setting.setText(_translate("MainWindow", "PRESSURE/FLOW"))
        self.relay_setting.setText(_translate("MainWindow", "RELAY"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/ENTER YOUR IMAGE PATH\"/></p></body></html>"))

class Worker(QtCore.QThread):
    valueFound = QtCore.pyqtSignal(int, name="valueFound")
    valuefound2 = QtCore.pyqtSignal(int, name="valueFound2")
    GAIN =2/3
    c1 = 525.4
    c2 = 28152
    Relay_1 = 27

    def __init__(self, parent=None):
        super(Worker,self).__init__(parent)
        self.runFlag = False
        self.i2c = busio.I2C(board.SCL,board.SDA)
        self.adc = ADS1115(self.i2c)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Relay_1, GPIO.OUT)
        GPIO.output(self.Relay_1, GPIO.HIGH)
        GPIO.output(self.Relay_1, GPIO.LOW)

    def startThread(self):
        self.runFlag = True
        self.start()

    def stopThread(self):
        self.runFlag = False

    def Pressure_Reading(self):
        self.sleep(0.02)
        r0 = self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
        r1 = self.adc.read_adc(0, gain = self.GAIN, data_rate =None)
        Pressure_Volts = r0*94.72436287
        Pressure_adc = r1*(self.c1/self.c2)

        self.sleep(0.02)
        r01= self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
        r11= self.adc.read_adc(0, gain = self.GAIN, data_rate =None)
        Pressure_Volts2 = r01*94.72436287
        Pressure_adc2 = r11*(self.c1/self.c2)

        self.sleep(0.02)
        r02= self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
        r12= self.adc.read_adc(0, gain = self.GAIN, data_rate =None)
        Pressure_Volts3 = r02*94.72436287
        Pressure_adc3 = r12*(self.c1/self.c2)

        self.sleep(0.02)
        r03 = self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
        r13 = self.adc.read_adc(0, gain = self.GAIN, data_rate =None)
        Pressure_Volts4 = r03*94.72436287
        Pressure_adc4 = r13*(self.c1/self.c2)

        self.sleep(0.02)
        r04= self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
        r14= self.adc.read_adc(0, gain = self.GAIN, data_rate =None)
        Pressure_Volts5 = r04*94.72436287
        Pressure_adc5 = r14*(self.c1/self.c2)

        Pressure_Volts_Avg = (Pressure_Volts+Pressure_Volts2+Pressure_Volts3+Pressure_Volts4+Pressure_Volts5)/5
        Pressure_adc_Avg = (Pressure_adc+Pressure_adc2+Pressure_adc3+Pressure_adc4+Pressure_adc5)/5
        Pressure_Avg = (Pressure_Volts_Avg+Pressure_adc_Avg)/2
        return Pressure_adc_Avg


    def Pressure_Reading2(self):
        r2 = self.adc.read_adc(1,gain = self.GAIN, data_rate = None)
        Pressure2_adc = r2*(self.c1/self.c2)
        r21 = self.adc.read_adc(1,gain = self.GAIN, data_rate = None)
        Pressure2_adc2 = r21*(self.c1/self.c2)
        r22 = self.adc.read_adc(1,gain = self.GAIN, data_rate = None)
        Pressure2_adc3 = r22*(self.c1/self.c2)
        r23 = self.adc.read_adc(1,gain = self.GAIN, data_rate = None)
        Pressure2_adc4 = r23*(self.c1/self.c2)

        r24 = self.adc.read_adc(1,gain = self.GAIN, data_rate = None)
        Pressure2_adc5 = r24*(self.c1/self.c2)

        Pressure_2_Avg = (Pressure2_adc+Pressure2_adc2+Pressure2_adc3+Pressure2_adc4+Pressure2_adc5)/5
        return Pressure_2_Avg

    @QtCore.pyqtSlot()
    def Relay_1_On(self):
        GPIO.output(self.Relay_1, GPIO.HIGH)

    @QtCore.pyqtSlot()
    def Relay_1_Off(self):
        GPIO.output(self.Relay_1, GPIO.LOW)

    @QtCore.pyqtSlot()
    def Relay_1_On_Delay(self, val):
        self.sleep(val)
        GPIO.output(self.Relay_1,GPIO.HIGH)

    def run(self):
        while self.runFlag:
            self.valueFound.emit(self.Pressure_Reading())
            self.valueFound2.emit(self.Pressure_Reading2())


class ControlMainWindow(QtWidgets.QMainWindow):
    Relay_1_On = QtCore.pyqtSignal()
    Relay_1_Off = QtCore.pyqtSignal()
    Relay_1_Delay_On = QtCore.pyqtSignal(int)

    def __init__(self,parent=None):
        super(ControlMainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #HOMEPAGE PUSHBUTTONS
        self.ui.relay_home.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.settings_home.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
    #RELAY PAGE PUSHBUTTONS
        self.ui.settings_relay.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pressure_relay.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.On_Button.clicked.connect(self.OnSwitch)
        self.ui.Off_Button.clicked.connect(self.OffSwitch)

    #SETTINGS PAGE PUSHBUTTONS
        self.ui.pressure_setting.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.relay_setting.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))

        self.worker = Worker(self)
        self.worker.valueFound.connect(self.OnValueFound)
        self.worker.valueFound2.connect(self.OnValueFound2)

        self.Relay_1_On.connect(self.worker.Relay_1_On)
        self.Relay_1_Off.connect(self.worker.Relay_1_Off)
        self.Relay_1_Delay_On.connect(self.worker.Relay_1_On_Delay)

        self.worker.startThread()

    def closeEvent(self, value):
        self.worker.stopThread()
        while self.worker.isRunning():
            pass
        event.accept()

    def OnValueFound(self, value):
        self.ui.lcdNumber1.display(value)
        self.ui.lcdNumber_7.display(value)

        if 100 < value < 300:
            self.ui.lcdNumber1.setStyleSheet("""QLCDNumber {/*background-color: 'green'; */ border-image: url(/home/pi/A3 Display/TransducerControl/Good_Pressure.png) ;color: green;}""")
            self.ui.lcdNumber_7.setStyleSheet("""QLCDNumber {/*background-color: 'green'; */ border-image: url(/home/pi/A3 Display/TransducerControl/Good_Pressure.png) ;color: green;}""")
        else:
            self.ui.lcdNumber1.setStyleSheet("""QLCDNumber {/*background-color:red; */ border-image: url(/home/pi/A3 Display/TransducerControl/Bad_Pressure2.png);color: black;}""")
            self.ui.lcdNumber_7.setStyleSheet("""QLCDNumber {/*background-color:red; */ border-image: url(/home/pi/A3 Display/TransducerControl/Bad_Pressure2.png);color: black;}""")

    def OnValueFound2(self, value):
        self.ui.lcdNumber2.display(value)
        self.ui.lcdNumber_8.display(value)
        if 100 < value < 300:
            self.ui.lcdNumber2.setStyleSheet("""QLCDNumber {/*background-color: green;*/ border-image: url(/home/pi/A3 Display/TransducerControl/Good_Pressure.png); color: black;}""")
            self.ui.lcdNumber_8.setStyleSheet("""QLCDNumber {/*background-color: green;*/ border-image: url(/home/pi/A3 Display/TransducerControl/Good_Pressure.png); color: black;}""")
        else:
            self.ui.lcdNumber2.setStyleSheet("""QLCDNumber {/*background-color:red;*/ border-image: url(/home/pi/A3 Display/TransducerControl/Bad_Pressure2.png); color: black;}""")
            self.ui.lcdNumber_8.setStyleSheet("""QLCDNumber {/*background-color:red;*/ border-image: url(/home/pi/A3 Display/TransducerControl/Bad_Pressure2.png); color: black;}""")


    def OnSwitch(self):
        self.Relay_1_On.emit()

    def OffSwitch(self):
        self.Relay_1_Off.emit()

    def Delay_Switch(self):
        self.Relay_1_Delay_On.emit(5)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
