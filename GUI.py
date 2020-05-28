from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import sys
class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(600,300)
        self.setWindowTitle("COVID statystyki")
        self.show()

        etykieta1 = QLabel("Wykres", self)
        etykieta2 = QLabel("Wczytywanie pliku", self)
        etykieta3 = QLabel("Wybor danych", self)
        etykieta4 = QLabel("Opcje wyswoetlania", self)

        Uklad = QGridLayout()
        Uklad.addWidget(etykieta1, 0,0)
        Uklad.addWidget(etykieta2, 0,1)
        Uklad.addWidget(etykieta3, 1,0)
        Uklad.addWidget(etykieta4,1,1)

        self.setLayout(Uklad)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Covidstat()
    sys.exit(app.exec_())