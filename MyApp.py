# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import MyWindow


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.myWidget = MyWindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton('Zmiana &napisu')
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        # setText ustawia nowy napis
        self.myWidget.label.setText('Zmieniony napis')
        # wyłacza przycisk
        self.button.setDisabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('Program PyQt OOP')
    window.resize(1000, 70)  # minimalne rozmiary okna
    window.show()
    sys.exit(app.exec_())
