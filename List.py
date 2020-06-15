from PyQt5.QtWidgets import QListWidget

from Instances import graph, var
from Interfaces import DataInterface
from Sections import Section


class List:
    def __init__(self, x, y, x_span, y_span):
        self._x = x
        self._y = y
        self._x_span = x_span
        self._y_span = y_span

    def add_list(self):
        list_widget = QListWidget()
        var.get_layout().addWidget(list_widget, self._x, self._y, self._x_span, self._y_span)


class ListOfCountries(List):
    def add_list(self):
        list_widget = QListWidget()
        if var.get_valid():
            var.set_list_of_countries(DataInterface().get_country_list(var.get_data_path()))
            for country in var.get_list_of_countries():
                list_widget.addItem(country)
            list_widget.itemClicked.connect(lambda item: self.action_on_click(item))
        var.get_layout().addWidget(list_widget, self._x, self._y, self._x_span, self._y_span)

    def action_on_click(self, item):
        if item.text() in var.get_list_of_countries_to_show_on_plot():
            var.rm_list_of_counters_to_show_on_plot(item.text())
        else:
            var.a_list_of_counters_to_show_on_plot(item.text())
        ListOfChosenCountries(self._x, self._y + 1, self._x_span, self._y_span).add_list()
        graph.add_section()


class ListOfChosenCountries(List):
    def add_list(self):
        list_widget = QListWidget()
        if var.get_valid():
            for country in sorted(var.get_list_of_countries_to_show_on_plot()):
                list_widget.addItem(country)
            list_widget.itemClicked.connect(lambda item: self.action_on_click(item))
        var.get_layout().addWidget(list_widget, self._x, self._y, self._x_span, self._y_span)

    def action_on_click(self, item):
        if item.text() in var.get_list_of_countries_to_show_on_plot():
            var.rm_list_of_counters_to_show_on_plot(item.text())
        else:
            var.a_list_of_counters_to_show_on_plot(item.text())
        ListOfChosenCountries(self._x, self._y, self._x_span, self._y_span).add_list()
        graph.add_section()


class SectionListOfCountries(Section):
    def add_section(self):
        ListOfCountries(self._x, self._y, self._x_span, self._y_span).add_list()
        ListOfChosenCountries(self._x, self._y + 1, self._x_span, self._y_span).add_list()
