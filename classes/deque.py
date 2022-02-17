class deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index of the
        list that is representing the Deque.

        The runtime is linear, or O(n) because every time you insert into the front of
        a list, all the other items need to shift one position to the right."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes an item as a parameter and appends that item to the end of the list that
        is representing the Deque.

        The runtime is constant because appending to the end of a list happens in constant time."""

        self.items.append(item)

    def remove_front(self, item):
        """Removes and returns the 0th index of the list, whiich represents the front of the deque.

        The runtime is linear, or O(n) because when we remove an item from the 0th index, all the
        other items have to shift one position to the left."""

        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self, item):
        """Removes and returns the last item of the list, which represents the rear of the deque.

        The runtime is constant because we are simply indexing the end of a list."""

        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """Returns the first item in the list, which represents the front of the deque.

        The runtime is constant because we are simply returning the first index of the list."""

        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """Returns the last item in the list, which represents the rear of the deque.

        The runtime is constant because all we are doing is returning the last index of the list."""

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list which is representing the deque.

         The runtime is constant because all we are doing is finding the length."""

        return len(self.items)

    def is_empty(self):
        """Checks to see if the list representing our deque is empty, returns true if it is and false if it is not.

        Runtime is constant because all we are doing is checking a boolean expression."""

        return self.items == []