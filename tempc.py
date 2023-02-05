import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType("tempconv_menu.ui")[0]

class TemperatureConverterWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btnCtoF_clicked)
        self.btnFtoC.clicked.connect(self.btnFtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btnCtoF_clicked)
        self.actionF_to_C.triggered.connect(self.btnFtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btnCtoF_clicked(self):
        cel = self.editCel.text()
        try:
            cel = float(self.editCel.text())
        except:
            cel = -273.15
            cel_text = '%.2f' % cel
            self.editCel.setText(cel_text)
        fahr = cel * 9 / 5 + 32
        fahr_text = '%.2f' % fahr
        self.editFar.setText(fahr_text)

    def btnFtoC_clicked(self):
        fahr = self.editCel.text()
        try:
            fahr = float(self.editFar.text())
        except:
            fahr = 0
            fahr_text = '%.2f' % fahr
            self.editFar.setText(fahr_text)
        cel = (fahr - 32) * 5 / 9.0
        cel_text = '%.2f' % cel
        self.editCel.setText(cel_text)
    
    def menuExit_selected(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
myWindow = TemperatureConverterWindow()
myWindow.show()
app.exec_()