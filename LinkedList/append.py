class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.length += 1
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        self.length += 1

    def insert(self, index, data):
        newNode = Node(data)
        current = self.head
        counter = 0
        if index >= self.length:
            return self.append(data)
        while counter != index - 1:
            current = current.next
            counter += 1

        leader = current
        holdingPointer = leader.next
        leader.next = newNode
        newNode.next = holdingPointer

    def remove(self, index):
        current = self.head
        counter = 0
        if index >= self.length:
            raise ValueError("Index out of bound!")
        if index < 0:
            raise ValueError("Index must be a positive integer!")
        while counter != index - 1:
            current = current.next
            counter += 1
        leader = current
        unWantedNode = leader.next
        leader.next = unWantedNode.next

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("->".join(elements))


myHead = LinkedList()
myHead.append(1)
myHead.append(2)
myHead.insert(1, 100)
myHead.insert(10, 200)
myHead.remove(1)
myHead.remove(-10)
myHead.display()
