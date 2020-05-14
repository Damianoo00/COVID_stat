def read_data_for_country(filename, countries):
    countries_data = dict()
    with open(filename, "r") as f:
        for line in f:
            may_be_country = line.split(",")[1]
            if may_be_country in countries:
                line = line.strip()
                v_of_cases = write_cases_to_vec(line)
                countries_data[may_be_country] = v_of_cases
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
        print(list_of_coutries)


#print(read_data_for_country("time_series_covid19_confirmed_global.csv", "Poland"))
get_list_of_countries("time_series_covid19_confirmed_global.csv")