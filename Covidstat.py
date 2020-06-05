from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import struct_lib, interfaces, activities

DATA_PATH = "time_series_covid19_confirmed_global.csv"
LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT = []
IS_LEGEND = True
X_LOGARYTHMIC = False
Y_LOGARYTHMIC = False

class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()
    
    def getfile(self):
        global DATA_PATH
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
        'c:\\',"(*.csv)")
        DATA_PATH = fname[0]
        
        
        

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
        
        plot = show_plot(Uklad)
        
# Sekcja wczytywania danych
        afbtn = QPushButton("wczytaj dane")
        afbtn.clicked.connect(self.getfile)        
        Uklad.addWidget(afbtn, 0,1)
        
# Sekcja listy państw   
        global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
        listWidget = QListWidget(self)
        listWidget.resize(100,75)
        list_of_countries = interfaces.Data_interface.get_country_list(DATA_PATH)
        for country in list_of_countries:
                listWidget.addItem(country)
        listWidget.itemClicked.connect(lambda item: listclickedaction(item, Uklad))
        Uklad.addWidget(listWidget, 1,0)
        print(LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT)
        
# Sekcja Checkbox
        
        b1 = QCheckBox("Legenda")
        b1.setChecked(True)
        b1.stateChanged.connect(lambda:checkboxstate(Uklad,"legend"))
        b2 = QCheckBox("Skala logarytmiczna osi X")
        b2.stateChanged.connect(lambda:checkboxstate(Uklad,"x_log"))
        b3 = QCheckBox("Skala logarytmiczna osi y")
        b3.stateChanged.connect(lambda:checkboxstate(Uklad,"y_log"))
        Uklad.addWidget(b1,2,1)
        Uklad.addWidget(b2,3,1)
        Uklad.addWidget(b3,4,1)
             
        self.setLayout(Uklad)
        





def show_plot(Uklad):
        graphWidget = pg.PlotWidget()
        graphWidget.setBackground('w')
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        if IS_LEGEND == True:
            graphWidget.addLegend()
        
        i = 0
        for country in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                print(country)
                y = interfaces.Data_interface.list_of_cases_in_country(country)
                x = [i for i in range(len(y))]
                graphWidget.plot(x, y, pen=colors[i%8], name=country)
                i = i+1
        graphWidget.setLogMode(X_LOGARYTHMIC, Y_LOGARYTHMIC)
        
        
        
        
        
        Uklad.addWidget(graphWidget, 0,0)

def listclickedaction(item, Uklad):
        global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
        if item.text() in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(item.text())
        else:
                LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(item.text())
        show_plot(Uklad)

def checkboxstate(Uklad, s):

        global IS_LEGEND
        global X_LOGARYTHMIC
        global Y_LOGARYTHMIC
        if s == "legend":
                if IS_LEGEND == True:
                        IS_LEGEND = False
                        show_plot(Uklad)
                else:
                        IS_LEGEND = True
                        
        if s == "x_log":
                if X_LOGARYTHMIC == False:
                        X_LOGARYTHMIC = True
                else:
                        X_LOGARYTHMIC = False
        if s == "y_log":
                if Y_LOGARYTHMIC == True:
                        Y_LOGARYTHMIC = False
                else:
                        Y_LOGARYTHMIC = True
        show_plot(Uklad)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Covidstat()
    sys.exit(app.exec_())

