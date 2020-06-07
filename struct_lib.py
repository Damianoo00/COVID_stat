from PyQt5.QtWidgets import QApplication ,QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QListWidget, QCheckBox, QButtonGroup
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from Covidstat import Uklad
DATA_PATH = ""
LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT = []
IS_LEGEND = True
X_LOGARYTHMIC = False
Y_LOGARYTHMIC = False
class Section:
        def __init__(self,x,y):
                self.x = x
                self.y =y
class Section_add_file(Section):
        def __init__(self, x, y, text_on_button):
                super().__init__(x,y)
                self.text_on_button = text_on_button
                
                self.show_section()
        def show_section(self):
                afbtn = QPushButton(self.text_on_button)
                afbtn.clicked.connect(Covidstat.getfile)
                return afbtn
class Section_list_of_countries(Section):
        def __init__(self, x, y):
                super().__init__(x,y)
                
                
                self.add_section()
        def add_section(self):
                global Uklad
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                #print(DATA_PATH)
                listWidget = QListWidget()
                listWidget.resize(100,75)
                try:
                        list_of_countries = interfaces.Data_interface.get_country_list(DATA_PATH)
                        for country in list_of_countries:
                                        listWidget.addItem(country)
                        listWidget.itemClicked.connect(lambda item: self.action_on_click(item, Uklad))
                except:
                        print("Problem z danymi")
                Uklad.addWidget(listWidget, self.y,self.x)
        def action_on_click(self, item, Uklad):
                global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
                if item.text() in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(item.text())
                else:
                        LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(item.text())
        
                Section_Graph(1,1).add_section()
class Section_checkbox(Section):
        def __init__(self, x, y):
                super().__init__(x,y)

        def add_section(self):
                b1 = QCheckBox("Legenda")
                b1.setChecked(True)
                b1.stateChanged.connect(lambda:self.checkboxstate(Uklad,"legend"))
                b2 = QCheckBox("Skala logarytmiczna osi X")
                b2.stateChanged.connect(lambda:self.checkboxstate(Uklad,"x_log"))
                b3 = QCheckBox("Skala logarytmiczna osi y")
                b3.stateChanged.connect(lambda:self.checkboxstate(Uklad,"y_log"))
                Uklad.addWidget(b1,2,1)
                Uklad.addWidget(b2,3,1)
                Uklad.addWidget(b3,4,1)
        def checkboxstate(self,Uklad, s):

                global IS_LEGEND
                global X_LOGARYTHMIC
                global Y_LOGARYTHMIC
                if s == "legend":
                        if IS_LEGEND == True:
                                IS_LEGEND = False
                                #Section_Graph(1,1).add_section()
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
                Section_Graph(1,1).add_section()
class Section_Graph(Section):
        def __init__(self,x,y):
                super().__init__(x,y)
        def add_section(self):
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