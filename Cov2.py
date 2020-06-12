from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
import sys
import warnings

from File import SectionAddFile
from AlertLabel import SectionAddAlertLabel
from Checkbox import SectionCheckbox
from Graph import SectionGraph
from List import SectionListOfCountries
from ShowOptions import SectionChoseOptionOfShowGraph
from Vars import Variables as Var


# TODO opisy błędów w polu alert; czynność odświeża to pole (albo dodaje nowy błąd albo pole puste)
# TODO axis log reformat
# TODO porządki nieużywanego kodu
# TODO o co chodzi z tymi connect? (linijki: 80, 131, 213, 264)
# TODO listy obok siebie
# TODO na pewno coś jeszcze
# TODO czy ta ścieżka musi tu (gdzieś) być?


class Covidstat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(1200, 600)
        self.setWindowTitle("COVID statystyki")
        self.show()

        layout = QGridLayout()
        global_val_obj = Var()
        global_val_obj.set_layout(layout)
        SectionGraph(0, 0, 1, 3).add_section(global_val_obj)
        SectionAddFile(1, 2, 1, 1).add_section(global_val_obj)
        SectionListOfCountries(2, 0, 1, 1).add_section(global_val_obj)
        SectionCheckbox(2, 2, 1, 1).add_section(global_val_obj)
        SectionAddAlertLabel(1, 0, 1, 2).add_alert(global_val_obj.get_alert(),global_val_obj)
        SectionChoseOptionOfShowGraph(3, 0, 1, 2).add_section(global_val_obj)

        self.setLayout(layout)
        


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    app = QApplication(sys.argv)
    window = Covidstat()
    sys.exit(app.exec_())
