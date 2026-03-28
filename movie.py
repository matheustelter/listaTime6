class Movie:
    # Para poder anexar apenas UM valor por nodo criamos uma classe filme
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getName(self):
        return self.name

    def getYear(self):
        return self.year