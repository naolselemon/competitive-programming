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

    def push(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holdingPointer = self.top
            self.top = new_node
            self.top.next = holdingPointer
        self.length += 1

        return self

    def pop(self):

        if self.length == 0:
            print("There is no element to pop!")
            return None

        holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1
        return holdingPointer

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" | ".join(elements))


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.peek()
    stack.display()
    stack.pop()
    stack.display()
