# from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication([])
app.setStyle('Fusion')  # dostępne style: Windows, WindowsVista, Macintosh
app.setStyleSheet('QPushButton {margin: 3ex;}')
# palette = QPalette
# # ustawienie koloru czerwony
# palette.setColor(QPalette.ButtonText, Qt.red)
# app.setPalette(palette)  # zmiana koloru
# button = QPushButton('Hello World')

window = QWidget()
layout = QVBoxLayout()  # utworzenie layoutu (QHBoxLayout dla układania w rząd)
layout.addWidget(QPushButton('Top'))    # dodajemy przycisk Top w layoucie
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)    # mówimy aby okno używało layoutu
window.show()   # wyświetlenie okna
app.exec_()
