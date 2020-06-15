from PyQt5.QtWidgets import QPushButton

from Instances import graph, var
from Sections import Section


class Button:
    def __init__(self, x, y, x_span, y_span, text):
        self._x = x
        self._y = y
        self._x_span = x_span
        self._y_span = y_span
        self._text = text

    def add_button(self):
        button = QPushButton(self._text)
        button.clicked.connect(lambda: self.action_on_click())
        var.get_layout().addWidget(button, self._x, self._y, self._x_span, self._y_span)

    def action_on_click(self):
        pass


class CasesButton(Button):
    def action_on_click(self):
        var.set_diff(False)
        graph.add_section()


class DiffButton(Button):
    def action_on_click(self):
        var.set_diff(True)
        graph.add_section()


class SectionGraphDisplayOption(Section):
    def add_section(self):
        CasesButton(self._x, self._y, self._x_span, self._y_span, "Liczba odnotowanych przypadków").add_button()
        DiffButton(self._x + 1, self._y, self._x_span, self._y_span, "Dzienny przyrost nowych przypadków").add_button()
