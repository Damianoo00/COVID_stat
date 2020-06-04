from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import struct_lib, interfaces

def show_plot(Uklad,Is_legend, Is_logaritmic_scale):
        graphWidget = pg.PlotWidget()
        y = interfaces.Data_interface.list_of_cases_in_country("China")
        x = [i for i in range(len(y))]
        y2 = interfaces.Data_interface.list_of_cases_in_country("US")
        x2 = [i for i in range(len(y))]
        
        graphWidget.setBackground('w')
        if Is_legend == True:
            graphWidget.addLegend()
        
        graphWidget.plot(x, y, pen='r', name="China")
        graphWidget.plot(x2, y2, pen='b', name="US")
        Uklad.addWidget(graphWidget, 0,0)

def checkboxstate(Uklad, Is_checked, s):
    if s == "Legenda":
        if Is_checked == True:
            show_plot(Uklad, True, False)
        else:
            show_plot(Uklad, False, False)

def listactiv(Uklad, countryname):
    print(countryname)
    #graphWidget = pg.PlotWidget()
    #y = interfaces.Data_interface.list_of_cases_in_country("China")
    #x = [i for i in range(len(y))]      
    #graphWidget.setBackground('w')
    #graphWidget.addLegend()   
    #graphWidget.plot(x, y, pen='r', name=countryname)
    #Uklad.addWidget(graphWidget, 0,0)

