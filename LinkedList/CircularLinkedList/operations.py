"""
Circular linked list implementation with common operations.
The last node always points back to the head node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            self.length += 1
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            self.length += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.length += 1

    def insert(self, index, data):
        if index < 0 or index > self.length:
            print("Index out of bound!")
            return

        if index == 0:
            self.prepend(data)
            return

        if index == self.length:
            self.append(data)
            return

        new_node = Node(data)
        current = self.head
        counter = 0

        while counter != index - 1:
            current = current.next
            counter += 1

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def remove(self, index):
        if not self.head:
            print("List is empty!")
            return

        if index < 0 or index >= self.length:
            print("Index out of bound!")
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        if index == 0:
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return

        current = self.head
        counter = 0

        while counter != index - 1:
            current = current.next
            counter += 1

        unwanted_node = current.next
        current.next = unwanted_node.next

        if unwanted_node == self.tail:
            self.tail = current

        self.length -= 1

    def lookup(self, data):
        current = self.head

        for index in range(self.length):
            if current.data == data:
                return index
            current = current.next

        return -1

    def display(self):
        if not self.head:
            print("List is empty!")
            return

        current = self.head
        elements = []

        for _ in range(self.length):
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> (back to head)")


if __name__ == "__main__":
    my_list = CircularLinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.prepend(0)
    my_list.insert(2, 100)
    my_list.remove(1)
    my_list.display()
    print(my_list.lookup(100))
