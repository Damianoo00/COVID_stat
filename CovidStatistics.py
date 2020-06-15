from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
import sys
import warnings

from Instances import *


# TODO "connect" zaadoptować z PyQt4 do PyQt5, żeby nie podkreślało (Button, Checkbox, File, List x2)
# TODO podzielić kod w ReadFile (!!!)


class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(1200, 600)
        self.setWindowTitle("COVID statystyki")
        self.show()

        layout = QGridLayout()
        var.set_layout(layout)
        graph.add_section()
        file.add_section()
        list_of.add_section()
        checkbox.add_section()
        label.add_section()
        button.add_section()

        self.setLayout(layout)


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    app = QApplication(sys.argv)
    window = Covidstat()
    sys.exit(app.exec_())
