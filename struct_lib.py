from PyQt5.QtWidgets import QWidget,QGridLayout, QLabel, QListWidget
class Okno(QWidget):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    
class Section(Okno):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
class List_of_countries:
    pass
    

class Section_add_file(Section):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__etykieta = "add_fle"
    def add(self, arg, etykieta2):
        return arg.addWidget(etykieta2,self.__x, self.__y)

class Section_list_of_countries(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(x, y)
        self.__etykieta = "list_of_countries"

class Section_Graph(Section):
    def __init__(self, etykieta, x, y):
        super().__init__(x, y)
        self.__etykieta = "wykres"

class Section_checkbox(Section):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__etykieta = "checkbox"
    


class List_of_all_countries:
    pass
class List_of_chosen_countries:
    pass




        
