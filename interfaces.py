from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import read_file
from Covidstat import ValuesError

class Data_interface:
    def get_country_list(filepath):
        r=read_file.From_File.get_list_of_countries(filepath)
        return r
    def get_cases_for_countrys_in_list(filepath, countrynames):
        try:
            r=read_file.From_File.read_data_for_country(filepath, Data_interface.listtostring(countrynames))
        except:
            ValuesError.show_alert("Wykres")
            #print("[Błąd]: Nie można rozczytać wartości")
            r = 0

        return r
    def get_cases_for_countrys_in_string(filepath, countrynames):
        try:
            r =read_file.From_File.read_data_for_country(filepath, countrynames)
        except:
            #print("[Błąd]: Nie można rozczytać wartości")
            ValuesError.show_alert("Wykres")
            r =0
        return r
    def listtostring(lista):
        s=""
        for country in lista:
            s=s+","+country
        return s
    def list_of_cases_in_country(countryname, filepath):
        dicta = Data_interface.get_cases_for_countrys_in_string(filepath, countryname)
        return dicta[countryname]
    
        