from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog

from Instances import label, list_of, var, graph
from Interfaces import DataInterface
from Sections import Section


class AddFile(QWidget):
    def __init__(self, x, y, x_span, y_span, text):
        super().__init__(parent=None)
        self._x = x
        self._y = y
        self._x_span = x_span
        self._y_span = y_span
        self._text = text

    def add_add_file(self):
        add_file_button = QPushButton(self._text)
        add_file_button.clicked.connect(lambda: self.action_on_click())
        var.get_layout().addWidget(add_file_button, self._x, self._y, self._x_span, self._y_span)

    def action_on_click(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'time_series_covid19_confirmed_global.csv', "(*.csv)")
        var.set_valid(DataInterface().validation(filename[0]))
        var.clear_lists()
        var.set_data_path(filename[0])
        list_of.add_section()
        label.add_section()
        if not var.get_valid():
            graph.add_section()


class SectionAddFile(Section):
    def add_section(self):
        AddFile(self._x, self._y, self._x_span, self._y_span, "Wczytaj moje dane").add_add_file()
