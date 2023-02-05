# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Program PyQt')
window.resize(800, 70)  # minimalne rozmiary okna
# tagi pozwalają na formowanie np. tabel i innych elementów HTML
label = QtWidgets.QLabel('<center>Witajcie w PyQt!</center>')

# symbol & pozwoli skorzystać z klawisza i Alt dla zamknięcia
btnQuit = QtWidgets.QPushButton('&Zamknij okno')

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)

vbox.addWidget(btnQuit)
window.setLayout(vbox)  # dodaje kontener vbox do okna window
btnQuit.clicked.connect(app.quit)   # połączenie z sygnałem buttona
window.show()
sys.exit(app.exec_())
