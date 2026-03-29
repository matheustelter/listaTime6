from linked_list import LinkedList
from movie import *

def inputMovie() -> Movie:
    name = input("Digite o nome do filme a inserir: ")

    year = int(input("Digite o ano do filme a inserir: "))
    while(year > 2026 or year < 1):
        year = int(input("Ano inválido! Digite o ano do filme a inserir: "))

    categoriesInput = input("Digite as categorias, se houver várias digite no formato '1 2 3': ")
    categories = [int(x) for x in categoriesInput.split()]

    while(True):
        categoriesValid = True
        for category in categories:
            if category < 0 or category > len(categoriesList):
                categoriesInput = input("Categoria(s) inválida(s)! Digite as categorias, se houver várias digite no formato '1, 2, 3': ")
                categories = [int(x) for x in categoriesInput.split()]
                categoriesValid = False

        if categoriesValid:
            break
        

    return Movie(name, year, categories)   
    

def startMenu(movieList: LinkedList):
    option = "1"

    while option != "0":
        print("\n    MENU DA LISTA DE FILMES ENCADEADA")
        print("1 - Inserir no Início")
        print("2 - Inserir no Fim")
        print("3 - Mostrar Lista")
        print("4 - Pesquisar Filme na Lista")
        print("5 - Excluir no Início")
        print("6 - Excluir no Fim")
        print("7 - Ordenar lista")
        print("0 - Sair do Programa")

        option = input("\nDigite o número referente a opção: ")
        print()

        if option == "1":
            movie = inputMovie()

            wasInserted = movieList.insertAtBeginning(movie)

            if wasInserted:
                print(f"Filme {movie.name}({movie.year}) inserido no início da lista!")

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
                    print(f"{currentMovie.toString()}")
 
            print("--------------------------")
 
        elif option == "4":
            name = input("Digite o filme que deseja PESQUISAR, por nome: ")
            movies = movieList.getList()

            if movies is None:
                print(f"Falha! Lista vazia.")
            else:
                found = False

                position = 1
                for movie in movies:
                    if movie.name == name:
                        print(f"Sucesso! Filme {name} foi achado na posição {position}.")
                        found = True
                        break
                    position += 1

                if found == False:
                    print(f"Falha! Filme {name} não encontrado na lista.")
            

        elif option == "5":
            removedValue = movieList.deleteFromBeginning()

            if removedValue is None:
                print("A lista está vazia! Não há nada para excluir no início.")
            else:
                print(f"Valor {removedValue.name} removido do início!")

        elif option == "6":
            removedValue = movieList.deleteFromEnd()

            if removedValue is None:
                print("A lista está vazia! Não há nada para excluir no fim.")
            else:
                print(f"Valor {removedValue.name} removido do fim!")

        elif option == "7":
            wasSorted = sortMovieList(movieList)

            if not wasSorted:
                print("A lista não precisa ser ordenada (está vazia ou tem só 1 elemento).")
            else:
                print("Lista ordenada com sucesso!")

        elif option == "0":
            print("Encerrando o programa... Até logo!")

        else:
            print("Opção inválida! Por favor, tente novamente.")
    

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


def main():
    moviesList = LinkedList()

    startMenu(moviesList)


if __name__ == "__main__":
    main()
