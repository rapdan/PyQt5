# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
# import sys # Wariant 1


# app = QtWidgets.QApplication(sys.argv)
# window = uic.loadUi("dialog.ui")

# window.btnQuit.clicked.connect(app.quit)
# window.show()
# sys.exit(app.exec_())

# Wariant 2 z class
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("dialog.ui", self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Program PyQt OOP')
    window.show()
    sys.exit(app.exec_())
