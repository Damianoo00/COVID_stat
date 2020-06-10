
from Exceptions import ValuesError
from Read2 import FromFile


class DataInterface:
    def get_country_list(self, filepath):
        r = FromFile().get_list_of_countries(filepath)
        return r

    def get_cases_for_countries_in_list(self, filepath, countrynames):
        try:
            r = FromFile().read_data_for_countries(filepath, DataInterface().listtostring(countrynames))
        except:
            print(ValuesError("Wykres"))
            r = 0

        return r

    def get_cases_for_countries_in_string(self, filepath, country_names):
        try:
            r = FromFile().read_data_for_countries(filepath, country_names)
        except:
            print(ValuesError("Wykres"))
            r = 0
        return r

    def listtostring(self, lista):
        s = ""
        for country in lista:
            s = s + "," + country
        return s

    def list_of_cases_in_country(self, countryname, filepath):
        dicta = DataInterface().get_cases_for_countries_in_string(filepath, countryname)
        return dicta[countryname]
