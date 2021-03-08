from collections import deque

class VisitQueue:
    def __init__(self):
        self.deque = deque()

    def add(self, node):
        self.deque.append(node)

    def dequeue(self):
        return self.deque.popleft()

    def isEmpty(self):
        return len(self.deque) == 0

    def __str__(self):
        return str(self.deque)
