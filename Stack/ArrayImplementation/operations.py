"""Array implementation of stack operations"""


class Stack:
    def __init__(self):
        self.array = []
        self.length = 0

    def peek(self):
        total = len(self.array)
        print(self.array[total - 1])

    def push(self, data):
        self.array.append(data)
        self.length += 1
        print(self.array)

    def pop(self):
        self.array.pop()
        self.length -= 1
        print(self.array)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop()
    stack.peek()
