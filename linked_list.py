class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def display_node(self):
        print(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display_list(self):
        if self.is_empty():
            print("Lista vazia!")
            return None

        current = self.head

        while current is not None:
            current.display_node()
            current = current.next

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"Valor {value} inserido no início!")

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            print(f"Valor {value} inserido no fim (lista estava vazia)!")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        print(f"Valor {value} inserido no fim!")

    def delete_from_beginning(self):
        if self.is_empty():
            print("A lista estÃ¡ vazia! NÃ£o hÃ¡ nada para excluir no início.\n")
            return None

        removed_node = self.head
        self.head = self.head.next

        print(f"Valor {removed_node.value} removido do início!")
        return removed_node.value

    def delete_from_end(self):
        if self.is_empty():
            print("A lista estÃ¡ vazia! NÃ£o hÃ¡ nada para excluir no início.")
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

    def search_list(self, searched_value):
        if self.is_empty():
            print("Lista vazia. Nada para achar!")
            return None

        current = self.head
        position = 0

        while current is not None:
            if current.value == searched_value:
                print(f"Sucesso! Valor {searched_value} foi achado na posição {position}.")
                return current
            current = current.next
            position += 1

        print(f"Falha! Valor {searched_value} não encontrado na lista.")
        return None

    def sort_list(self):
        if self.is_empty() or self.head.next is None:
            print("A lista não precisa ser ordenada (está vazia ou tem só 1 elemento).\n")
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
