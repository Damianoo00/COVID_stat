import numpy as np
from Exceptions import ValuesError


class FromFile:

    def read_data_for_countries(self, filename, countries):
        countries_data = dict()

        with open(filename, "r") as f:
            for line in f:
                may_be_country = line.split(",")[1]

                if may_be_country in countries:
                    line = line.strip()
                    v_of_cases = self.write_cases_to_vec(line)

                    if may_be_country in countries_data:
                        sum_data = list(map(np.add, countries_data[may_be_country], v_of_cases))
                        countries_data[may_be_country] = sum_data
                    else:
                        countries_data[may_be_country] = v_of_cases

        return countries_data

    def write_cases_to_vec(self, data_line):
        unimportant_columns = 4
        v_of_cases = data_line.split(",")[unimportant_columns:]
        v_of_cases = [int(val) for val in v_of_cases]
        return v_of_cases

    def get_list_of_countries(self, filename):
        try:
            it = 0
            with open(filename, "r") as f:
                list_of_countries = []
                for line in f:
                    if it > 0:
                        name = line.split(",")[1]
                        list_of_countries.append(name)
                    it = it + 1
                return sorted(list(set(list_of_countries)))
        except FileNotFoundError:
            print(ValuesError("Interfejs danych"))
