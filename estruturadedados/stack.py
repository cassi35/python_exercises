from collections import deque
stack = deque()
stack.append('htpps://google.com')
stack.append('htpps://youtube.com')
stack.append('htpps://gmail.com')
stack.append('htpps://faecbook.com')
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_impty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def print(self):
        if self.is_impty():
            print(self.container)
            return
        return None

pilha = Stack()
for i in stack:
    pilha.push(i)
