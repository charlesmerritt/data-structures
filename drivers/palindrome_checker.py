class IsPalindrome:

    def main(self) -> None:
        string = input("Enter a string to check: ")
        if IsPalindrome.reverse(string) == string:
            print(f"{string} is a palindrome.")
            return
        print(f"{string} is not a palindrome.")

    @staticmethod
    def reverse(string: str) -> str:
        reverse_string = ""
        for character in string[ : :-1]:
            reverse_string += character
        return reverse_string

run = IsPalindrome()
run.main()

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        self.items.pop(0)

    def remove_rear(self):
        self.items.pop()

    def size(self):
        return len(self.items)

def check_palindrome(input_str):

    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2: # Size of 1 or 0 means string is a palindrome
        front_item = my_d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False

    return True

print(check_palindrome("racecar"))
print(check_palindrome("oranges"))