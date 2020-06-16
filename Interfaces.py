from ReadFile import FromFile, Validation


class DataInterface:
    def validation(self, file_path):
        valid = Validation().check_data_path(file_path)
        if valid:
            valid = Validation().validate_data(file_path)
        return valid

    def get_country_list(self, file_path):
        r = FromFile().get_list_of_countries(file_path)
        return r

    def get_cases_for_country_in_string(self, file_path, country_names):
        r = FromFile().read_data_for_countries(file_path, country_names)
        return r

    def list_of_cases_in_country(self, country_name, file_path):
        dictionary = self.get_cases_for_country_in_string(file_path, country_name)
        return dictionary[country_name]
