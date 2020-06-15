from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from Instances import var
from Sections import Section


class Label:
    def __init__(self, x, y, x_span, y_span, text):
        self._x = x
        self._y = y
        self._x_span = x_span
        self._y_span = y_span
        self._label = QLabel()
        self._text = text

    def add_label(self):
        self._label.clear()
        self._label.setText(self._text)
        self._label.setAlignment(Qt.AlignCenter)
        var.get_layout().addWidget(self._label, self._x, self._y, self._x_span, self._y_span)


class AlertLabel(Label):
    def add_label(self):
        self._label.clear()
        self._label.setText(self._text)
        self._label.setAlignment(Qt.AlignCenter)
        self._label.setStyleSheet('color: red; background: white; border: 1px solid black;')
        var.get_layout().addWidget(self._label, self._x, self._y, self._x_span, self._y_span)
        var.clear_alert()


class TextLabel(Label):
    def add_label(self):
        self._label.clear()
        self._label.setText(self._text)
        self._label.setAlignment(Qt.AlignCenter)
        self._label.setStyleSheet('color: black; background: white; border: 1px solid black;')
        var.get_layout().addWidget(self._label, self._x, self._y, self._x_span, self._y_span)
        var.clear_alert()


class SectionLabel(Section):

    def add_section(self):
        if var.get_valid():
            var.no_alert()
            TextLabel(self._x, self._y, self._x_span, self._y_span + 1, var.get_alert()).add_label()
        else:
            AlertLabel(self._x, self._y, self._x_span, self._y_span + 1, var.get_alert()).add_label()
        TextLabel(self._x + 1, self._y, self._x_span, self._y_span, "Lista państw").add_label()
        TextLabel(self._x + 1, self._y + 1, self._x_span, self._y_span, "Lista wybranych państw").add_label()
