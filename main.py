from linked_list import LinkedList


def main():
    linkedList = LinkedList()

    option = "1"

    while option != "0":
        print("\n    MENU DA LISTA ENCADEADA")
        print("1 - Inserir no InÃ­cio")
        print("2 - Inserir no Fim")
        print("3 - Mostrar Lista")
        print("4 - Pesquisar Valor")
        print("5 - Excluir no InÃ­cio")
        print("6 - Excluir no Fim")
        print("7 - Ordenar lista")
        print("0 - Sair do Programa")

        option = input("\nDigite o nÃºmero referente a opÃ§Ã£o: ")
        print()

        if option == "1":
            value = int(input("Digite o nÃºmero para inserir no INÃCIO: "))
            linkedList.insertAtBeginning(value)

        elif option == "2":
            value = int(input("Digite o nÃºmero para inserir no FIM: "))
            linkedList.insertAtEnd(value)

        elif option == "3":
            print("--- Elementos da Lista ---")
            linkedList.displayList()
            print("--------------------------")

        elif option == "4":
            value = int(input("Digite o nÃºmero que deseja PESQUISAR: "))
            linkedList.searchList(value)

        elif option == "5":
            linkedList.deleteFromBeginning()

        elif option == "6":
            linkedList.deleteFromEnd()

        elif option == "7":
            linkedList.sortList()

        elif option == "0":
            print("Encerrando o programa... AtÃ© logo!")

        else:
            print("OpÃ§Ã£o invÃ¡lida! Por favor, tente novamente.")


if __name__ == "__main__":
    main()
