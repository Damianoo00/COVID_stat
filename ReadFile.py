import numpy as np
from Exceptions import ValuesError, CommaError, NoDataError, UnevenDataError, NonNumericError, NumericNameError, \
    NoCountryError
from Instances import var


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
        start = False
        with open(filename, "r") as f:
            list_of_countries = []
            for line in f:
                if start:
                    name = line.split(",")[1]
                    list_of_countries.append(name)
                else:
                    start = True
            return sorted(list(set(list_of_countries)))


class Validation:

    def validate_data(self, filename):
        try:
            counter = 1
            valid = True
            state = True
            unimportant_columns = 4
            comma_check = set()
            data_len_check = set()
            with open(filename, "r") as f:
                for line in f:
                    if not state:
                        name = line.split(",")[1]
                        valid = self.check_countries(name, valid)
                        digits = line.split(",")[unimportant_columns:]
                        digits[-1] = digits[-1].strip("\n")
                        valid = self.check_digits(digits[1:], valid)
                        [comma_check, valid] = self.check_additional_comma(comma_check, digits, name, counter, valid)
                        [data_len_check, valid] = self.check_data_length(data_len_check, digits, valid)
                    else:
                        state = False
                    if not valid:
                        break
                    counter = counter + 1
                if state:
                    raise NoDataError("Pusty skoroszyt")
            return valid
        except NoDataError as e:
            var.add_alert(e)
            return False
        except (FileNotFoundError, UnicodeDecodeError, IndexError):
            var.add_alert(ValuesError("Dane"))
            return False

    def check_data_path(self, filename):
        try:
            if filename == "":
                raise NoDataError("Ścieżka pliku")
            else:
                return True
        except NoDataError as e:
            var.add_alert(e)
            return False

    def check_countries(self, country, valid):
        try:
            if country:
                try:
                    float(country)
                    raise NumericNameError("Państwa")
                except ValueError:
                    return valid
            else:
                raise NoCountryError("Państwa")
        except (NoCountryError, NumericNameError) as e:
            var.add_alert(e)
            return False

    def check_digits(self, digits, valid):
        try:
            digits = list(filter(None, digits))
            for i in digits:
                if i.isdigit():
                    pass
                else:
                    raise NonNumericError("Dane")
            return valid
        except NonNumericError as e:
            var.add_alert(e)
            return False

    def check_data_length(self, data_len_check, digits, valid):
        try:
            data_len_check.add(len([s for s in digits if s.isdigit()]))
            if len(data_len_check) > 1:
                raise UnevenDataError("Dane liczbowe")
            return [data_len_check, valid]
        except UnevenDataError as e:
            var.add_alert(e)
            return [data_len_check, False]

    def check_additional_comma(self, comma_check, digits, name, counter, valid):
        try:
            comma_check.add(len(digits))
            if len(comma_check) > 1:
                if list(comma_check)[1] - list(comma_check)[0] == 1:
                    if not name:
                        name = 'NoName'
                    raise CommaError("Dane w wierszu " + str(counter) +
                                     " dla regionu/państwa (kolumna A/B) '" + str(name.strip(' " ')) + "'")
                else:
                    raise UnevenDataError("Dane")
            return [comma_check, valid]
        except (UnevenDataError, CommaError) as e:
            var.add_alert(e)
            return [comma_check, False]
