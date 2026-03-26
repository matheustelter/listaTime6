from linked_list import LinkedList


def main():
    linkedList = LinkedList()

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

        option = input("\nDigite o número referente a opÃ§ão: ")
        print()

        if option == "1":
            value = int(input("Digite o número para inserir no INÍCIO: "))
            wasInserted = linkedList.insertAtBeginning(value)

            if wasInserted:
                print(f"Valor {value} inserido no início!")

        elif option == "2":
            value = int(input("Digite o número para inserir no FIM: "))
            wasInserted = linkedList.insertAtEnd(value)

            if wasInserted:
                print(f"Valor {value} inserido no fim!")

        elif option == "3":
            print("--- Elementos da Lista ---")
            values = linkedList.displayList()

            if values is None:
                print("Lista vazia!")
            else:
                for currentValue in values:
                    print(currentValue)

            print("--------------------------")

        elif option == "4":
            value = int(input("Digite o número que deseja PESQUISAR: "))
            foundNode = linkedList.searchList(value)

            if foundNode is None:
                print(f"Falha! Valor {value} não encontrado na lista.")
            else:
                position = 0
                currentNode = linkedList.head

                while currentNode is not foundNode:
                    currentNode = currentNode.next
                    position += 1

                print(f"Sucesso! Valor {value} foi achado na posiÃ§ão {position}.")

        elif option == "5":
            removedValue = linkedList.deleteFromBeginning()

            if removedValue is None:
                print("A lista está vazia! Não há nada para excluir no início.")
            else:
                print(f"Valor {removedValue} removido do início!")

        elif option == "6":
            removedValue = linkedList.deleteFromEnd()

            if removedValue is None:
                print("A lista está vazia! Não há nada para excluir no fim.")
            else:
                print(f"Valor {removedValue} removido do fim!")

        elif option == "7":
            wasSorted = linkedList.sortList()

            if not wasSorted:
                print("A lista não precisa ser ordenada (está vazia ou tem só 1 elemento).")
            else:
                print("Lista ordenada com sucesso!")

        elif option == "0":
            print("Encerrando o programa... Até logo!")

        else:
            print("Opção inválida! Por favor, tente novamente.")


if __name__ == "__main__":
    main()
