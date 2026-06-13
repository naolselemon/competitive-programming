"""Queue using array implementation"""

import array


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = array.array("i", [0] * capacity)
        self.size = 0
        self.front = 0
        self.rear = 0

    def peek(self):
        if self.size == 0:
            return -1
        return self.queue[self.front]

    def enqueue(self, data):

        if self.size >= self.capacity:
            print("Queue is full")

        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empaty!")
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data


if __name__ == "__main__":
    queue = Queue(10)

    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
