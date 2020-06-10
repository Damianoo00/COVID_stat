class Errors(Exception):
    def __init__(self, place):
        self._message = "[Błąd][" + str(place) + "]: "
        super().__init__(self._message)


class NoDataError(Errors):
    def __str__(self):
        self._message = self._message + "Brak danych"
        return self._message


class ValuesError(Errors):
    def __str__(self):
        self._message = self._message + "Błędne wartości"
        return self._message
