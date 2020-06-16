class Errors(Exception):
    def __init__(self, place):
        self._message = "[Błąd][" + str(place) + "]: "
        super().__init__(self._message)


class NoDataError(Errors):
    def __str__(self):
        self._message = self._message + "Brak danych"
        return self._message


class NonNumericError(Errors):
    def __str__(self):
        self._message = self._message + "Dane nienumeryczne"
        return self._message


class ValuesError(Errors):
    def __str__(self):
        self._message = self._message + "Błędne dane i/lub wartości"
        return self._message


class CommaError(Errors):
    def __str__(self):
        self._message = self._message + "Możliwy przecinek w nazwie lub różnica o 1 w długościach wierszy danych"
        return self._message


class UnevenDataError(Errors):
    def __str__(self):
        self._message = self._message + "Wiersze danych różnej długości"
        return self._message


class NumericNameError(Errors):
    def __str__(self):
        self._message = self._message + "Nazwa państwa nie zawiera liter"
        return self._message


class NoCountryError(Errors):
    def __str__(self):
        self._message = self._message + "Brak co najmniej jednej nazwy państwa"
        return self._message
