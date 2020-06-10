from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, \
    QListWidget, QCheckBox, QButtonGroup

from Exceptions import NoDataError
from Inter2 import DataInterface
from lib_repair import pyqtgraph as pg
import sys
import numpy as np

DATA_PATH = ""
ALERT = ""
LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT = []
IS_LEGEND = True
X_LOGARITHMIC = False
Y_LOGARITHMIC = False
Uklad = None
DIFF = False


class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        global Uklad
        self.resize(600, 300)
        self.setWindowTitle("COVID statystyki")
        self.show()

        Uklad = QGridLayout()
        SectionGraph(0, 0).add_section()
        SectionAddFile(0, 1).add_section()
        SectionListOfCountries(0, 1).add_section()
        SectionCheckbox(1, 1).add_section()
        # Section_alert_label(0,2).add_alert(ALERT)
        SectionChoseOptionOfShowGraph(2, 0).add_section()

        self.setLayout(Uklad)


class Section:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add_section(self):
        pass


class SectionChoseOptionOfShowGraph(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        CasesButton(self._x, self._y, "Liczba odnotowanych przypadków").add_button()
        DiffButton(self._x + 1, self._y, "Dzienny przyrost nowych przypadków").add_button()


class Button:
    def __init__(self, x, y, text):
        self._x = x
        self._y = y
        self._text = text

    def add_button(self):
        button = QPushButton(self._text)
        button.clicked.connect(lambda: self.action_on_click())
        Uklad.addWidget(button, self._x, self._y)

    def action_on_click(self):
        pass


class CasesButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)

    def action_on_click(self):
        global DIFF
        DIFF = False
        SectionGraph(0, 0).add_section()


class DiffButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)

    def action_on_click(self):
        global DIFF
        DIFF = True
        SectionGraph(0, 0).add_section()


class AddFileButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)

    def action_on_click(self):
        global DATA_PATH
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '~/Documents/Edukacja/PO/PO_proj', "(*.csv)")

        DATA_PATH = fname[0]
        SectionListOfCountries(0, 1).add_section()


class AddFile(QWidget):
    def __init__(self, x, y, text):
        super().__init__(parent=None)
        self._x = x
        self._y = y
        self._text = text

    def add_add_file(self):
        add_file_button = QPushButton(self._text)
        add_file_button.clicked.connect(lambda: self.action_on_click())
        Uklad.addWidget(add_file_button, self._x, self._y)

    def action_on_click(self):
        global DATA_PATH
        filename = QFileDialog.getOpenFileName(self, 'Open file',
                                               '~/Documents/Edukacja/PO/PO_proj', "(*.csv)")

        DATA_PATH = filename[0]
        SectionListOfCountries(0, 1).add_section()


class SectionAddFile(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        AddFile(self._x, self._y, "Wczytaj moje dane").add_add_file()


class Label:
    def __init__(self, x, y, text):
        self._x = x
        self._y = y
        self.text = text

    def add_label(self):
        label = QLabel(self.text)
        Uklad.addWidget(label, self._y, self._x)


class AlertLabel(Label):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)

    def add_label(self):
        label = QLabel(self.text)
        label.setStyleSheet('color: red')
        Uklad.addWidget(label, self._y, self._x)


class SectionLabel(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        pass


class SectionAlertLabel(SectionLabel):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_alert(self, text_of_alert):
        AlertLabel(self._x, self._y, text_of_alert).add_label()


class List:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add_list(self):
        list_widget = QListWidget()
        Uklad.addWidget(list_widget, self._x, self._y)


class ListOfCountries(List):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_list(self):

        global Uklad
        global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
        list_widget = QListWidget()
        try:
            list_of_countries = DataInterface().get_country_list(DATA_PATH)

            check_data_path()
            for country in list_of_countries:
                list_widget.addItem(country)
            list_widget.itemClicked.connect(lambda item: self.action_on_click(item))
        except NoDataError:
            print(NoDataError("Lista"))
        except:
            print(NoDataError("lista"))

        Uklad.addWidget(list_widget, self._y, self._x)

    def action_on_click(self, item):

        global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
        if item.text() in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
            LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(item.text())
        else:
            LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(item.text())

        SectionGraph(0, 0).add_section()


def ff():
    global DIFF
    DIFF = False
    SectionGraph(0, 0).add_section()


def fff():
    global DIFF
    DIFF = True
    SectionGraph(0, 0).add_section()


class SectionListOfCountries(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        ListOfCountries(self._x, self._y).add_list()


class Checkbox:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.boolean = boolean = None
        self.text = text = None

    def add_checkbox(self):
        b1 = QCheckBox(self.text)
        b1.setChecked(self.boolean)
        b1.stateChanged.connect(lambda: self.action_on_click())
        Uklad.addWidget(b1, self._x, self._y)

    def action_on_click(self):
        pass


class LegendCheckbox(Checkbox):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.boolean = True
        self.text = "legenda"

    def action_on_click(self):
        global IS_LEGEND
        if IS_LEGEND:
            IS_LEGEND = False
        else:
            IS_LEGEND = True
        SectionGraph(0, 0).add_section()


class YAxisLogCheckbox(Checkbox):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.boolean = False
        self.text = "Skala logarytmiczna na Osi Y"

    def action_on_click(self):
        global Y_LOGARITHMIC
        if Y_LOGARITHMIC:
            Y_LOGARITHMIC = False
        else:
            Y_LOGARITHMIC = True
        SectionGraph(0, 0).add_section()


class XAxisLogCheckbox(Checkbox):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.boolean = False
        self.text = "Skala logarytmiczna na Osi X"

    def action_on_click(self):
        global X_LOGARITHMIC
        if X_LOGARITHMIC:
            X_LOGARITHMIC = False
        else:
            X_LOGARITHMIC = True
        SectionGraph(0, 0).add_section()


class SectionCheckbox(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        LegendCheckbox(self._y, self._x).add_checkbox()
        YAxisLogCheckbox(self._y + 1, self._x).add_checkbox()
        XAxisLogCheckbox(self._y + 2, self._x).add_checkbox()


class SectionGraph(Section):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_section(self):
        GraphOfCountries(self._x, self._y).add_graph()


class Graph(SectionGraph):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_graph(self):
        graph_widget = pg.PlotWidget()

        Uklad.addWidget(graph_widget, self._x, self._y)


class GraphOfCountries(Graph):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add_graph(self):
        global ALERT
        global LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT
        graph_widget = pg.PlotWidget()
        graph_widget.setBackground('w')
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        if IS_LEGEND:
            graph_widget.addLegend()

        i = 0
        try:
            check_data_path()
            for country in LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT:
                y = DataInterface().list_of_cases_in_country(country, DATA_PATH)
                if DIFF:
                    y = np.diff(np.array(DataInterface().list_of_cases_in_country(country, DATA_PATH))).tolist()
                x = [i for i in range(len(y))]
                graph_widget.plot(x, y, pen=colors[i % len(colors)], name=country)
                graph_widget.setLogMode(X_LOGARITHMIC, Y_LOGARITHMIC)
                i = i + 1
        except:
            print(NoDataError("Wykres"))
            del LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT[len(LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT) - 1]

        Uklad.addWidget(graph_widget, self._x, self._y)


def check_data_path():
    if DATA_PATH == "":
        print(NoDataError("Plik"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Covidstat()
    sys.exit(app.exec_())
