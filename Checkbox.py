from PyQt5.QtWidgets import QCheckBox

from Instances import var, graph
from Sections import Section


class Checkbox:
    def __init__(self, x, y, x_span, y_span):
        self._x = x
        self._y = y
        self._x_span = x_span
        self._y_span = y_span
        self.boolean = None
        self.text = None

    def add_checkbox(self):
        b1 = QCheckBox(self.text)
        b1.setChecked(self.boolean)
        b1.stateChanged.connect(lambda: self.action_on_click())
        var.get_layout().addWidget(b1, self._x, self._y, self._x_span, self._y_span)

    def action_on_click(self):
        pass


class LegendCheckbox(Checkbox):
    def __init__(self, x, y, x_span, y_span):
        super().__init__(x, y, x_span, y_span)
        self.boolean = True
        self.text = "Legenda"

    def action_on_click(self):
        if var.get_is_legend():
            var.set_is_legend(False)
        else:
            var.set_is_legend(True)
        graph.add_section()


class YAxisLogCheckbox(Checkbox):
    def __init__(self, x, y, x_span, y_span):
        super().__init__(x, y, x_span, y_span)
        self.boolean = False
        self.text = "Skala logarytmiczna na osi Y"

    def action_on_click(self):
        if var.get_y_logarithmic():
            var.set_y_logarithmic(False)
        else:
            var.set_y_logarithmic(True)
        graph.add_section()


class XAxisLogCheckbox(Checkbox):
    def __init__(self, x, y, x_span, y_span):
        super().__init__(x, y, x_span, y_span)
        self.boolean = False
        self.text = "Skala logarytmiczna na osi X"

    def action_on_click(self):
        if var.get_x_logarithmic():
            var.set_x_logarithmic(False)
        else:
            var.set_x_logarithmic(True)
        graph.add_section()


class SectionCheckbox(Section):
    def add_section(self):
        LegendCheckbox(self._x, self._y, self._x_span, self._y_span).add_checkbox()
        YAxisLogCheckbox(self._x + 1, self._y, self._x_span, self._y_span).add_checkbox()
        XAxisLogCheckbox(self._x + 2, self._y, self._x_span, self._y_span).add_checkbox()
