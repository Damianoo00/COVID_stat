import numpy as np
class From_File:
        
    def read_data_for_country(filename, countries):
        countries_data = dict()
        licznik_powtorzen = 0
        with open(filename, "r") as f:
            for line in f:
                may_be_country = line.split(",")[1]
                if may_be_country in countries:
                    line = line.strip()
                    v_of_cases = From_File.write_cases_to_vec(line)
                    if licznik_powtorzen == 0:
                        countries_data[may_be_country] = v_of_cases
                    else:
                        countries_data[may_be_country] = (np.array(countries_data[may_be_country]) + np.array(v_of_cases)).tolist()

                    licznik_powtorzen = licznik_powtorzen+1
        return countries_data

    def write_cases_to_vec(data_line):
        unimportat_colums = 4
        v_of_cases = data_line.split(",")[unimportat_colums:]
        v_of_cases = [int(val) for val in v_of_cases]
        return v_of_cases    

    def get_list_of_countries(filename):
        with open(filename, "r") as f:
            list_of_coutries = []
            for line in f:
                list_of_coutries.append(line.split(",")[1])
            return sorted(list(set(list_of_coutries)))





