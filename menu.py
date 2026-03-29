import json
from pathlib import Path

from linked_list import LinkedList
from movie import Movie, categoriesList


def inputMovie() -> Movie:
    name = input("Digite o nome do filme a inserir: ")

    year = int(input("Digite o ano do filme a inserir: "))
    while year > 2026 or year < 1:
        year = int(input("Ano invalido! Digite o ano do filme a inserir: "))

    categoriesInput = input("Digite as categorias, se houver varias digite no formato '1 2 3': ")
    categories = [int(x) for x in categoriesInput.split()]

    while True:
        categoriesValid = True
        for category in categories:
            if category < 0 or category > len(categoriesList) - 1:
                categoriesInput = input(
                    "Categoria(s) invalida(s)! Digite as categorias, se houver varias digite no formato '1 2 3': "
                )
                categories = [int(x) for x in categoriesInput.split()]
                categoriesValid = False
                break

        if categoriesValid:
            break

    return Movie(name, year, categories)


def loadMoviesFromJson(movieList: LinkedList) -> int:
    filePathInput = input(
        "Digite o caminho do arquivo JSON ou pressione Enter para usar 'test_movies.json': "
    ).strip()
    filePath = Path(filePathInput) if filePathInput else Path("test_movies.json")

    if not filePath.exists():
        print(f"Arquivo '{filePath}' nao encontrado.")
        return 0

    try:
        with filePath.open("r", encoding="utf-8") as jsonFile:
            moviesData = json.load(jsonFile)
    except json.JSONDecodeError:
        print("Falha ao ler o JSON. Verifique se o arquivo esta bem formatado.")
        return 0
    except OSError:
        print("Falha ao abrir o arquivo informado.")
        return 0

    if not isinstance(moviesData, list):
        print("O JSON deve conter uma lista de filmes.")
        return 0

    insertedMovies = 0

    for item in moviesData:
        if not isinstance(item, dict):
            continue

        name = item.get("name")
        year = item.get("year")
        categories = item.get("categories")

        if not isinstance(name, str) or name.strip() == "":
            continue

        if not isinstance(year, int) or year < 1 or year > 2026:
            continue

        if not isinstance(categories, list) or len(categories) == 0:
            continue

        if not all(isinstance(category, int) for category in categories):
            continue

        if any(category < 0 or category > len(categoriesList) - 1 for category in categories):
            continue

        movieList.insertAtEnd(Movie(name.strip(), year, categories))
        insertedMovies += 1

    if insertedMovies == 0:
        print("Nenhum filme valido foi encontrado no arquivo.")
        return 0

    print(f"{insertedMovies} filme(s) carregado(s) com sucesso de '{filePath}'.")
    return insertedMovies


def startMenu(movieList: LinkedList):
    option = "1"

    while option != "0":
        print("\n    MENU DA LISTA DE FILMES ENCADEADA")
        print("1 - Inserir no Inicio")
        print("2 - Inserir no Fim")
        print("3 - Mostrar Lista")
        print("4 - Pesquisar Filme na Lista")
        print("5 - Excluir no Inicio")
        print("6 - Excluir no Fim")
        print("7 - Ordenar lista")
        print("8 - Carregar filmes de teste por JSON")
        print("0 - Sair do Programa")

        option = input("\nDigite o numero referente a opcao: ")
        print()

        if option == "1":
            movie = inputMovie()
            wasInserted = movieList.insertAtBeginning(movie)

            if wasInserted:
                print(f"Filme {movie.name}({movie.year}) inserido no inicio da lista!")

        elif option == "2":
            movie = inputMovie()
            wasInserted = movieList.insertAtEnd(movie)

            if wasInserted:
                print(f"Filme {movie.name}({movie.year}) inserido no fim da lista!")

        elif option == "3":
            print("--- Elementos da Lista ---")
            movies = movieList.getList()

            if movies is None:
                print("Lista vazia!")
            else:
                for currentMovie in movies:
                    print(currentMovie.toString())

            print("--------------------------")

        elif option == "4":
            openSearchMenu(movieList)

        elif option == "5":
            removedValue = movieList.deleteFromBeginning()

            if removedValue is None:
                print("A lista esta vazia! Nao ha nada para excluir no inicio.")
            else:
                print(f"Valor {removedValue.name} removido do inicio!")

        elif option == "6":
            removedValue = movieList.deleteFromEnd()

            if removedValue is None:
                print("A lista esta vazia! Nao ha nada para excluir no fim.")
            else:
                print(f"Valor {removedValue.name} removido do fim!")

        elif option == "7":
            wasSorted = sortMovieList(movieList)

            if not wasSorted:
                print("A lista nao precisa ser ordenada (esta vazia ou tem so 1 elemento).")
            else:
                print("Lista ordenada com sucesso!")

        elif option == "8":
            loadMoviesFromJson(movieList)

        elif option == "0":
            print("Encerrando o programa... Ate logo!")

        else:
            print("Opcao invalida! Por favor, tente novamente.")


def openSearchMenu(movieList: LinkedList):
    searchOption = "1"
    while searchOption != "0":
        print("\t1 - Pesquisar por nome")
        print("\t2 - Pesquisar por categoria")
        print("\t3 - Pesquisar por ano")
        print("\t0 - Voltar ao menu anterior")

        searchOption = input("\tDigite a opcao: ")

        if searchOption == "1":
            name = input("\tDigite o nome do filme que deseja pesquisar: ")
            movies = movieList.getList()

            if movies is None:
                print("\tFalha! Lista vazia.")
            else:
                position = 1
                for movie in movies:
                    if movie.name == name:
                        print(f"\tSucesso! Filme {movie.toString()}, posicao {position}.")
                        return
                    position += 1

                print(f"\tFalha! Filme {name} nao encontrado na lista.")

            return

        elif searchOption == "2":
            for i in range(len(categoriesList)):
                print(f"\t{i} - {categoriesList[i]}")

            categoryID = int(input("\tDigite o numero da categoria a pesquisar: "))

            if categoryID < 0 or categoryID > len(categoriesList) - 1:
                print("\tCategoria invalida!")
                return

            movies = movieList.getList()
            if movies is None:
                print("\tFalha! Lista vazia.")
                return

            moviesFound = False
            for movie in movies:
                if categoryID in movie.categories:
                    print(f"\t{movie.toString()}")
                    moviesFound = True

            if not moviesFound:
                print("\tNenhum filme registrado nesta categoria!")

            return

        elif searchOption == "3":
            year = int(input("\tDigite o ano a pesquisar: "))

            if year < 0 or year > 2026:
                print("\tAno invalido")
                return

            foundMovies = False
            movies = movieList.getList()

            if movies is None:
                print("\tFalha! Lista vazia.")
            else:
                for movie in movies:
                    if movie.year == year:
                        print(f"\tFilme {movie.toString()}")
                        foundMovies = True

            if not foundMovies:
                print(f"\tNenhum filme de {year} encontrado")

            return

        elif searchOption == "0":
            return

        else:
            print("\tOpcao invalida, tente novamente!\n")


def sortMovieList(movieList: LinkedList):
    if movieList.isEmpty() or movieList.head.next is None:
        return False

    swapped = True

    while swapped:
        swapped = False
        current = movieList.head

        while current.next is not None:
            if current.value.name > current.next.value.name:
                current.value, current.next.value = current.next.value, current.value
                swapped = True

            current = current.next

    return True
