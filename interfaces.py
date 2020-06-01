from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import struct_lib
import read_file

class Data_interface:
    def get_country_list(filepath):
        return read_file.From_File.get_list_of_countries(filepath)
    def get_cases_for_countrys_in_list(filepath, countrynames):
        return read_file.From_File.read_data_for_country(filepath, Data_interface.listtostring(countrynames))
    def get_cases_for_countrys_in_string(filepath, countrynames):
        return read_file.From_File.read_data_for_country(filepath, countrynames)
    def listtostring(lista):
        s=""
        for country in lista:
            s=s+","+country
        return s

class GUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


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
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        graphWidget.plot(hour, temperature)
        Uklad.addWidget(graphWidget, 0,0)
# Sekcja wczytywania danych        
        Uklad.addWidget(etykieta2, 0,1)
# Sekcja listy państw      
        listWidget = QListWidget(self)
        listWidget.resize(100,75)
        list_of_countries = Data_interface.get_country_list("time_series_covid19_confirmed_global.csv")
        for country in list_of_countries:
            listWidget.addItem(country)
        Uklad.addWidget(listWidget, 1,0)
# Sekcja Checkbox
        b1 = QCheckBox("Opcja 1")
        Uklad.addWidget(b1,1,1)
     
        self.setLayout(Uklad)
    