from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()  # tworzymy okno
label = QLabel('Hello World')
label.show()    # pokazuje okienko
app.exec_()     # dla zamknięcia przez użytkownika aplikacji
