class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def display(self):

        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print("->".join(elements))


head = LinkedList()
head.prepend(1)
head.prepend(2)
head.display()
