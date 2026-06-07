class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def append(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.length += 1
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode
        newNode.prev = lastNode
        self.length += 1

    def prepend(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.length += 1
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def insert(index, data):
        newNode = Node(data)
        counter = 0
        current = self.head

        if not current:
            self.head = newNode
            return

        while counter != index - 1:
            current = current.next
            counter += 1

        leader = current
        followingNode = leader.next
        leader.next = newNode
        newNode.prev = leader
        newNode.next = followingNode
        followingNode.prev = newNode

    def remove(self, index):
        counter = 0
        current = self.head
        if index >= self.length:
            print("Index out of bound")
            return
        if index < 0:
            print("Index cannot be negative")
            return

        while counter != index - 1:
            current = current.next
            counter += 1

        leader = current
        unWantedNode = leader.next
        leaderFollower = unWantedNode.next
        leader.next = leaderFollower
        leaderFollower.prev = leader
