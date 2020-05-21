import read_file

class Data_interface:
    def get_country_list(filepath):
        return read_file.From_File.get_list_of_countries(filepath)
    def get_cases_for_countrys_in_list(filepath, countrynames):
        return read_file.From_File.read_data_for_country(filepath, Data_interface.listtostring(countrynames))
    def get_cases_for_countrys_in_string(filepath, countrynames):
        return read_file.From_File.read_data_for_country(filepath, countrynames)
    def listtostring(lista):
        s=""
        for country in lista:
            s=s+","+country
        return s

if __name__ == "__main__":
    PATH = "time_series_covid19_confirmed_global.csv"
    
    print(Data_interface.get_country_list(PATH))
    print(Data_interface.get_cases_for_countrys_in_string(PATH, "Poland"))
    