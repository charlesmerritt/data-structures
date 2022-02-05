# Stacks are a LIFO structure, like a stack of pancakes.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is 0(1), or constant time, because appending to the end of a list happens in
        constant time.
        """

        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item from the list which is also the top item of the Stack.

        Runtime is constant time, or O(n), because all it does index to the last item of list.
        """
        return self.items.pop()

    def peek(self):
        """
        Returns the last item in the list which is also the item at the top of the Stack.

        Runtime is constant time, or O(n), because indexing into a list is done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the length of the list that is representing the Stack.

        Runtime is constant time, or O(n), because it only finds the length of a list.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value describing whether or not the stack is empty.

        Runtime is constant time, or O(n), because it is a simple test of equality.
        """
        return self.items == []
