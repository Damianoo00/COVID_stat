from PyQt5.QtWidgets import QApplication, QMessageBox ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
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
        
        

    def interface(self):
        global Uklad
        self.resize(600,300)
        self.setWindowTitle("COVID statystyki")
        self.show()

            
        
        Uklad = QGridLayout()
        
        Section_Graph(0,0).add_section()       

        Section_add_file(0,1).add_section()
           
        Section_list_of_countries(0,1).add_section()       

        Section_checkbox(1,1).add_section()

        Section_alert_label(0,2).add_alert("")

        self.setLayout(Uklad)




class Section:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def add_section():
                pass
class Add_file(QWidget):
        def __init__(self,x,y):
                super().__init__(parent = None)
                self.x = x
                self.y = y
                self.buttonlabel = "Wczytaj moje dane"
        def add_add_file(self):
                afbtn = QPushButton(self.buttonlabel)
                afbtn.clicked.connect(lambda: self.action_on_click())
                Uklad.addWidget(afbtn, 0,1)
        def action_on_click(self):
                global DATA_PATH
                fname = QFileDialog.getOpenFileName(self, 'Open file', 
                '~/Documents/Edukacja/PO/PO_proj',"(*.csv)")
        
                DATA_PATH = fname[0]
                Section_list_of_countries(0,1).add_section() 

class Section_add_file(Section):
        def __init__(self, x, y):
                super().__init__(x,y)
                
        def add_section(self):
                Add_file(self.x,self.y).add_add_file() 
class Label:
        def __init__(self,x,y,text):
                self.x = x
                self.y = y
                self.text = text
        def add_label(self):
                label = QLabel(self.text)
                Uklad.addWidget(label,self.y,self.x)
class Alert_label(Label):
        def __init__(self,x,y,text):
                super().__init__(x,y,text)
        def add_label(self):
                label = QLabel(self.text)
                label.setStyleSheet('color: red')
                Uklad.addWidget(label,self.y,self.x)
class Section_label(Section):
        def __init__(self, x, y):
                super().__init__(x,y)
        def add_section(self):
                pass
class Section_alert_label(Section_label):
        def __init__(self,x,y):
                super().__init__(x,y)
        def add_alert(self,text_of_alert):
                Alert_label(self.x,self.y, text_of_alert).add_label()

class List:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def add_list(self):
                listWidget = QListWidget()
                Uklad.addWidget(listWidget, self.x,self.y)
class List_of_countries(List):
        def __init__(self, x, y):
                super().__init__(x,y)
        def add_list(self):
                print(DATA_PATH)
                global Uklad
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                listWidget = QListWidget()
                
                list_of_countries = interfaces.Data_interface.get_country_list(DATA_PATH)
                try:
                        checkdatapath()
                        for country in list_of_countries:
                                listWidget.addItem(country)
                        listWidget.itemClicked.connect(lambda item: self.action_on_click(item))
                except NoDataError:
                        NoDataError.show_alert()
                
                Uklad.addWidget(listWidget, self.y,self.x)

        def action_on_click(self, item):
                
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                if item.text() in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(item.text())
                else:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(item.text())
                Section_Graph(0,0).add_section()

class Section_list_of_countries(Section):
        def __init__(self, x, y):
                super().__init__(x,y)
                
        def add_section(self):
                List_of_countries(self.x,self.y).add_list()
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
                legend_checkbox(self.y,self.x).add_checkbox()
                y_axis_log_checkbox(self.y+1,self.x).add_checkbox()
                x_axis_log_checkbox(self.y+2,self.x).add_checkbox()
        



class Section_Graph(Section):
        def __init__(self,x,y):
                super().__init__(x,y)
        def add_section(self):
                Graph_of_countries(self.x,self.y).addgraph()
                
class Graph(Section_Graph):
        def __init__(self, x,y):
                super().__init__(x,y)
        def addgraph(self):
                graphWidget = pg.PlotWidget()
                               
                Uklad.addWidget(graphWidget, self.x,self.y)

class Graph_of_countries(Graph):
        def __init__(self, x,y):
                super().__init__(x,y)
        def addgraph(self):
                graphWidget = pg.PlotWidget()
                graphWidget.setBackground('w')
                colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
                if IS_LEGEND == True:
                        graphWidget.addLegend()
                
                i = 0
                try:
                        for country in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                                y = interfaces.Data_interface.list_of_cases_in_country(country,DATA_PATH)
                                x = [i for i in range(len(y))]
                                graphWidget.plot(x, y, pen=colors[i%8], name=country)
                                graphWidget.setLogMode(X_LOGARYTHMIC,Y_LOGARYTHMIC)
                                i = i+1
                except:
                        ValuesError.show_alert()
                        print(DATA_PATH)

                        
                
                
                Uklad.addWidget(graphWidget, self.x,self.y)
def checkdatapath():
        if DATA_PATH == "":
                raise NoDataError
        
class Errors(Exception):
        pass
class NoDataError(Errors):
        def show_alert():
                print("[Błąd]: Brak danych")
class ValuesError(Errors):
        def show_alert():
                print("[Błąd]: Błędne wartości")

                
                        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Covidstat()
    sys.exit(app.exec_())

