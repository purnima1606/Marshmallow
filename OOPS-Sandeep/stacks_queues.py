l = [10, 20, 30, 40]
#
# print(l.pop())
# l.append(50)
# print(l.pop())


from collections import deque

d = deque(l)

d.append(50)
d.pop()

class Stack:

    def __init__(self):
        self.d = deque()        # self.d = []

    def push(self, item):
        self.d.append(item)

    def pop(self):
        return self.d.pop()

    def is_empty(self):
        return len(self.d) == 0

    def get_item(self, index):
        return self.d[index]


l = [10, 20, 30, 40]

q = deque(l)

q.append(50)        # l = [10, 20, 30, 40, 50]
q.popleft()

class Queue:

    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return len(self.q) == 0

    def peek(self, index):
        return self.q[index]


class Queue:

    def __init__(self):
        self.q = deque()

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.popleft()

    def is_empty(self):
        return len(self.q) == 0

    def peek(self, index):
        return self.q[index]










