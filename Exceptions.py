class Errors(Exception):
    def __init__(self, place):
        self._message = "[Błąd][" + str(place) + "]: "
        super().__init__(self._message)

    # def __str__(self):
    #     return self._message


class NoDataError(Errors):
    def __str__(self):
        self._message = self._message + "Brak danych"
        return self._message


class ValuesError(Errors):
    def __str__(self):
        self._message = self._message + "Błędne dane i/lub wartości"
        return self._message


class CommaError(Errors):
    def __str__(self):
        self._message = self._message + "Należy usunąć przecinek"
        return self._message


class UnevenDataError(Errors):
    def __str__(self):
        self._message = self._message + "Wiersze danych różnej długości"
        return self._message


