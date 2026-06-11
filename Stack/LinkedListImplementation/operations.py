class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        if self.length == 0:
            print("Stack is empty!")
            return

        print(self.top.data)
