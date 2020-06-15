class Variables:
    def __init__(self):
        self.__ALERT = "Należy wczytać plik -->"
        self.__DATA_PATH = ""
        self.__DIFF = False
        self.__IS_LEGEND = True
        self.__LIST_OF_COUNTRIES = []
        self.__LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT = []
        self.__LAYOUT = None
        self.__VALID = False
        self.__X_LOGARITHMIC = False
        self.__Y_LOGARITHMIC = False

    def get_alert(self):
        return self.__ALERT

    def add_alert(self, x):
        if not self.__ALERT:
            self.__ALERT = str(x)
        else:
            self.__ALERT = self.__ALERT + "\n" + str(x)

    def clear_alert(self):
        self.__ALERT = ""

    def no_alert(self):
        self.__ALERT = "No Errors"

    def get_data_path(self):
        return self.__DATA_PATH

    def set_data_path(self, x):
        self.__DATA_PATH = x

    def get_diff(self):
        return self.__DIFF

    def set_diff(self, x):
        self.__DIFF = x

    def get_is_legend(self):
        return self.__IS_LEGEND

    def set_is_legend(self, x):
        self.__IS_LEGEND = x

    def get_list_of_countries(self):
        return self.__LIST_OF_COUNTRIES

    def set_list_of_countries(self, x):
        self.__LIST_OF_COUNTRIES = x

    def get_list_of_countries_to_show_on_plot(self):
        return self.__LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT

    def a_list_of_counters_to_show_on_plot(self, x):
        self.__LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.append(x)

    def rm_list_of_counters_to_show_on_plot(self, x):
        self.__LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.remove(x)

    def clear_lists(self):
        self.__LIST_OF_COUNTRIES.clear()
        self.__LIST_OF_COUNTRIES_TO_SHOW_ON_PLOT.clear()

    def get_layout(self):
        return self.__LAYOUT

    def set_layout(self, x):
        self.__LAYOUT = x

    def get_valid(self):
        return self.__VALID

    def set_valid(self, x):
        self.__VALID = x

    def get_x_logarithmic(self):
        return self.__X_LOGARITHMIC

    def set_x_logarithmic(self, x):
        self.__X_LOGARITHMIC = x

    def get_y_logarithmic(self):
        return self.__Y_LOGARITHMIC

    def set_y_logarithmic(self, x):
        self.__Y_LOGARITHMIC = x
