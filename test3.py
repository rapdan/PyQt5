from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox

app = QApplication([])
app.setStyleSheet('QPushButton {margin: 2ex;}')
button = QPushButton('Kliknij')


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Kliknąłeś przycisk!')
    alert.exec_()


button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
