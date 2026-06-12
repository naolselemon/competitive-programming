"""Queue implementation with Linked list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            print("There is no in the list")
        print(self.first.data)

    def enqueue(self, data):
        new_node = Node(data)
        if self.first == self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):

        if self.length == 0:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1

