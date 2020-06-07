from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
from lib_repair import pyqtgraph as pg
import sys
import interfaces
import numpy as np


DATA_PATH = ""
LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT = []
IS_LEGEND = True
X_LOGARYTHMIC = False
Y_LOGARYTHMIC = False
Uklad = 0

class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()
    
    def getfile(self):
        global DATA_PATH
        try:        
                fname = QFileDialog.getOpenFileName(self, 'Open file', 
                '~/Documents/Edukacja/PO/PO_proj',"(*.csv)")
        
                DATA_PATH = fname[0]
        except:
                print("brak pliku")
        Section_list_of_countries(0,1).add_section()
        
        
        

    def interface(self):
        global Uklad
        self.resize(600,300)
        self.setWindowTitle("COVID statystyki")
        self.show()

            
        
        Uklad = QGridLayout()
# Sekcja Wykres 
        
        Section_Graph(0,0).add_section()       
# Sekcja wczytywania danych
        afbtn = QPushButton("wczytaj dane")
        afbtn.clicked.connect(self.getfile)
        #Section_add_file(0,1,"Wczytaj moje dane z pliku CSV")      
        Uklad.addWidget(afbtn, 0,1)      
# Sekcja listy państw   
        Section_list_of_countries(0,1).add_section()       
# Sekcja Checkbox
        Section_checkbox(2,1).add_section()
        #legend_checkbox(1 ,1).add_checkbox()
        self.setLayout(Uklad)




class Section:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def add_section():
                pass
class Section_add_file(Section):
        def __init__(self, x, y, text_on_button):
                super().__init__(x,y)
                self.text_on_button = text_on_button
                
        def show_section(self):
                afbtn = QPushButton(self.text_on_button)
                afbtn.clicked.connect(Covidstat.getfile)
                return afbtn
class Section_list_of_countries(Section):
        def __init__(self, x, y):
                super().__init__(x,y)
                
        def add_section(self):
                global Uklad
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                listWidget = QListWidget()
                listWidget.resize(100,75)
                try:
                        list_of_countries = interfaces.Data_interface.get_country_list(DATA_PATH)
                        for country in list_of_countries:
                                        listWidget.addItem(country)
                        listWidget.itemClicked.connect(lambda item: self.action_on_click(item))
                except:
                        print("Problem z danymi")
                Uklad.addWidget(listWidget, self.y,self.x)
        def action_on_click(self, item):
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                if item.text() in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(item.text())
                else:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(item.text())
        
                Section_Graph(0,0).add_section()
class Checkbox:
        def __init__(self,x,y):
                self.x = x
                self.y = y
                self.boolen = boolen = None
                self.text = text = None
                
        def add_checkbox(self):
                b1 = QCheckBox(self.text)
                b1.setChecked(self.boolen)
                b1.stateChanged.connect(lambda:self.action_on_click())
                Uklad.addWidget(b1,self.x,self.y)
        def action_on_click(self):
                pass
class legend_checkbox(Checkbox):
        def __init__(self,x,y):
                super().__init__(x,y)
                self.boolen = True
                self.text = "legenda"
        def action_on_click(self):
                global IS_LEGEND
                if IS_LEGEND == True:
                        IS_LEGEND = False
                else:
                        IS_LEGEND = True
                Section_Graph(0,0).add_section()
class y_axis_log_checkbox(Checkbox):
        def __init__(self,x,y):
                super().__init__(x,y)
                self.boolen = False
                self.text = "Skala logarytmiczna na Osi Y"
        def action_on_click(self):
                global Y_LOGARYTHMIC
                if Y_LOGARYTHMIC == True:
                        Y_LOGARYTHMIC = False
                else:
                        Y_LOGARYTHMIC = True
                Section_Graph(0,0).add_section()
class x_axis_log_checkbox(Checkbox):
        def __init__(self,x,y):
                super().__init__(x,y)
                self.boolen = False
                self.text = "Skala logarytmiczna na Osi X"
        def action_on_click(self):
                global X_LOGARYTHMIC
                if X_LOGARYTHMIC == True:
                        X_LOGARYTHMIC = False
                else:
                        X_LOGARYTHMIC = True
                Section_Graph(0,0).add_section()
class Section_checkbox(Section):
        def __init__(self, x, y):
                super().__init__(x,y)

        def add_section(self):
                legend_checkbox(1,1).add_checkbox()
                y_axis_log_checkbox(2,1).add_checkbox()
                x_axis_log_checkbox(3,1).add_checkbox()
        



class Section_Graph(Section):
        def __init__(self,x,y):
                super().__init__(x,y)
        def add_section(self):
                Graph(self.x,self.y).addgraph()
                
class Graph(Section_Graph):
        def __init__(self, x,y):
                super().__init__(x,y)
        def addgraph(self):
                graphWidget = pg.PlotWidget()
                graphWidget.setBackground('w')
                colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
                if IS_LEGEND == True:
                        graphWidget.addLegend()
                
                i = 0
                for country in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                        y = interfaces.Data_interface.list_of_cases_in_country(country,DATA_PATH)
                        x = [i for i in range(len(y))]
                        graphWidget.plot(x, y, pen=colors[i%8], name=country)
                        graphWidget.setLogMode(X_LOGARYTHMIC,Y_LOGARYTHMIC)
                        
                        i = i+1
                
                Uklad.addWidget(graphWidget, self.x,self.y)

                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Covidstat()
    sys.exit(app.exec_())

