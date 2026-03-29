categoriesList = [
    'Ação',
    'Terror',
    'Aventura',
    'Suspense',
    'Comédia',
    'Drama',
    'Ficção Cientifica',
    'Adulto'
]

class Movie:
    # Para poder anexar apenas UM valor por nodo criamos uma classe filme
    def __init__(self, name, year, categories):
        self.name = name                # string
        self.year = year                # int
        self.categories = categories    # array de int
        
    def toString(self):
        string = f"{self.name} ({self.year}) - "

        for c in self.categories:
            string = string + f"{categoriesList[c]} "

        return string