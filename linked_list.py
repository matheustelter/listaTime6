class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def displayList(self):
        if self.isEmpty():
            return None

        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return True

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.isEmpty():
            self.head = new_node
            return True

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return True

    def deleteFromBeginning(self):
        if self.isEmpty():
            return None

        removed_node = self.head
        self.head = self.head.next
        return removed_node.value

    def deleteFromEnd(self):
        if self.isEmpty():
            return None

        if self.head.next is None:
            removed_node = self.head
            self.head = None
            return removed_node.value

        current = self.head

        while current.next.next is not None:
            current = current.next

        removed_node = current.next
        current.next = None
        return removed_node.value

    def searchList(self, searchedValue):
        if self.isEmpty():
            return None

        current = self.head

        while current is not None:
            if current.value == searchedValue:
                return current
            current = current.next

        return None

    def sortList(self):
        if self.isEmpty() or self.head.next is None:
            return False

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True

                current = current.next

        return True
