from linked_list import LinkedList


def main():
    linked_list = LinkedList()

    option = "1"

    while option != "0":
        print("\n    MENU DA LISTA ENCADEADA")
        print("1 - Inserir no Início")
        print("2 - Inserir no Fim")
        print("3 - Mostrar Lista")
        print("4 - Pesquisar Valor")
        print("5 - Excluir no Início")
        print("6 - Excluir no Fim")
        print("7 - Ordenar lista")
        print("0 - Sair do Programa")

        option = input("\nDigite o número referente a opção: ")
        print()

        if option == "1":
            value = int(input("Digite o número para inserir no INÍCIO: "))
            linked_list.insert_at_beginning(value)

        elif option == "2":
            value = int(input("Digite o número para inserir no FIM: "))
            linked_list.insert_at_end(value)

        elif option == "3":
            print("--- Elementos da Lista ---")
            linked_list.display_list()
            print("--------------------------")

        elif option == "4":
            value = int(input("Digite o número que deseja PESQUISAR: "))
            linked_list.search_list(value)

        elif option == "5":
            linked_list.delete_from_beginning()

        elif option == "6":
            linked_list.delete_from_end()

        elif option == "7":
            linked_list.sort_list()

        elif option == "0":
            print("Encerrando o programa... Até logo!")

        else:
            print("Opção inválida! Por favor, tente novamente.")


if __name__ == "__main__":
    main()
