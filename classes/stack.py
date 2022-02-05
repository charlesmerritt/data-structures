# Stacks are a LIFO structure, like a stack of pancakes. This stack, has the functions pop, push, and is_empty.
# push simply adds an item to the top of the stack
# pop removes an item from the top of the stack
# is_empty returns a bool, true if the stack is empty and false if it is not.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
