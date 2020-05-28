from PyQt5.QtWidgets import QWidget,QGridLayout, QLabel, QListWidget
class Okno(QWidget):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    
class Section(Okno):
    def __init__(self, etykieta, x, y):
        self.__etykieta = etykieta
        self.__x = x
        self.__y = y
class List:
    l = [1,2,3,4]

class Section_add_file(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(etykieta, x, y)

class Section_list_of_countries(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(etykieta, x, y)


class Section_Graph(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(etykieta, x, y)

class Section_checkbox(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(etykieta, x, y)

class List_of_all_countries:
    pass
class List_of_chosen_countries:
    pass




        

