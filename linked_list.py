class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def displayNode(self):
        print(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def displayList(self):
        if self.isEmpty():
            print("Lista vazia!")
            return None

        current = self.head

        while current is not None:
            current.displayNode()
            current = current.next

    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"Valor {value} inserido no inÃ­cio!")

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.isEmpty():
            self.head = new_node
            print(f"Valor {value} inserido no fim (lista estava vazia)!")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        print(f"Valor {value} inserido no fim!")

    def deleteFromBeginning(self):
        if self.isEmpty():
            print("A lista estÃ¡ vazia! NÃ£o hÃ¡ nada para excluir no inÃ­cio.\n")
            return None

        removed_node = self.head
        self.head = self.head.next

        print(f"Valor {removed_node.value} removido do inÃ­cio!")
        return removed_node.value

    def deleteFromEnd(self):
        if self.isEmpty():
            print("A lista estÃ¡ vazia! NÃ£o hÃ¡ nada para excluir no inÃ­cio.")
            return None

        if self.head.next is None:
            removed_node = self.head
            self.head = None
            print(f"Valor {removed_node.value} removido do fim!")
            return removed_node.value

        current = self.head

        while current.next.next is not None:
            current = current.next

        removed_node = current.next
        current.next = None

        print(f"Valor {removed_node.value} removido do fim!")
        return removed_node.value

    def searchList(self, searched_value):
        if self.isEmpty():
            print("Lista vazia. Nada para achar!")
            return None

        current = self.head
        position = 0

        while current is not None:
            if current.value == searched_value:
                print(f"Sucesso! Valor {searched_value} foi achado na posiÃ§Ã£o {position}.")
                return current
            current = current.next
            position += 1

        print(f"Falha! Valor {searched_value} nÃ£o encontrado na lista.")
        return None

    def sortList(self):
        if self.isEmpty() or self.head.next is None:
            print("A lista nÃ£o precisa ser ordenada (estÃ¡ vazia ou tem sÃ³ 1 elemento).\n")
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True

                current = current.next

        print("Lista ordenada com sucesso!\n")
