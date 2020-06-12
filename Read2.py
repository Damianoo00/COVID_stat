import numpy as np
from Exceptions import ValuesError, CommaError, NoDataError, UnevenDataError


class FromFile:

    def read_data_for_countries(self, filename, country):
        countries_data = dict()
        with open(filename, "r") as f:
            for line in f:
                may_be_country = line.split(",")[1]
                if may_be_country in country:
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
            counter = 1
            with open(filename, "r") as f:
                list_of_countries = []
                for line in f:
                    if counter > 1:
                        name = line.split(",")[1]
                        if name.count('"') % 2 == 0:
                            list_of_countries.append(name)
                        else:
                            print(CommaError("Dane dla kraju/regionu '" + str(name.strip(' " '))
                                             + "' w wierszu " + str(counter)))

                    counter = counter + 1
                return sorted(list(set(list_of_countries)))
        # except (FileNotFoundError, UnicodeDecodeError, IndexError):
        except FileNotFoundError as e:
            print(e)

    # TODO podziel to!

    def validate_data(self, filename):
        try:
            valid = True
            unimportant_columns = 4
            length_check = set()
            with open(filename, "r") as f:
                state = True
                for line in f:
                    if not state:
                        digits = line.split(",")[unimportant_columns:]
                        digits[-1] = digits[-1].strip("\n")
                        valid = self.check_digits(digits[1:], valid)
                        [length_check, valid] = self.check_length(length_check, digits, valid)
                    else:
                        state = False
                    if not valid:
                        break
                if state:
                    raise NoDataError("Pusty skoroszyt")
            return valid
        except NoDataError as e:
            print(e)
            return False
        except (FileNotFoundError, UnicodeDecodeError, IndexError):
            print(ValuesError("Dane"))
            return False

    def check_data_path(self, filename):
        try:
            if filename == "":
                raise NoDataError("Ścieżka pliku")
            else:
                return True
        except NoDataError as e:
            print(e)
            return False

    def check_digits(self, digits, valid):
        try:
            digits = list(filter(None, digits))
            for i in digits:
                if i.isdigit():
                    pass
                else:
                    raise ValuesError("Dane")
            return valid
        except ValuesError as e:
            print(e)
            return False

    def check_length(self, length_check, digits, valid):
        try:
            length_check.add(len([s for s in digits if s.isdigit()]))
            if len(length_check) > 1:
                raise UnevenDataError("Dane")
            return [length_check, valid]
        except UnevenDataError as e:
            print(e)
            return [length_check, False]
