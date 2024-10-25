import queue,threading
from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    def print(self):
        print(self.buffer)
q = Queue()
q.enqueue('cassiano')
q.enqueue('maria')
q.enqueue('joao')
q.print()