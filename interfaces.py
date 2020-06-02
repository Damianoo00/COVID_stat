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
    def list_of_cases_in_country(countryname):
        dicta = Data_interface.get_cases_for_countrys_in_string("time_series_covid19_confirmed_global.csv", countryname)
        return dicta[countryname]
        