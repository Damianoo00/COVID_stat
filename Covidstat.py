from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import struct_lib, interfaces

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
# Sekcja Wykres 
        graphWidget = pg.PlotWidget()
        y = [30,32,34,32,33,31,29,32,35,45]
        x = [i for i in range(len(y))]
        graphWidget.plot(x, y)
        Uklad.addWidget(graphWidget, 0,0)
# Sekcja wczytywania danych        
        Uklad.addWidget(etykieta2, 0,1)
# Sekcja listy państw      
        listWidget = QListWidget(self)
        listWidget.resize(100,75)
        list_of_countries = interfaces.Data_interface.get_country_list("time_series_covid19_confirmed_global.csv")
        for country in list_of_countries:
            listWidget.addItem(country)
        Uklad.addWidget(listWidget, 1,0)
# Sekcja Checkbox
        b1 = QCheckBox("Opcja 1")
        Uklad.addWidget(b1,1,1)
     
        self.setLayout(Uklad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Covidstat()
    sys.exit(app.exec_())