# A class Len is defined that computes the length of a string and stores it in a field-sensitive member variable 'length'.
# The constructor takes a string as a parameter, and the get_length method returns the length of the string.
# The field sensitivity allows the 'length' member variable to store different values in different contexts.
# The code involves calling a separate function 'compute_length' to perform the length computation.
# The code also includes a nested class 'Nested' to demonstrate multiple depth in field sensitivity.


def compute_length(s):
    return len(s)


class Len:
    def __init__(self, s):
        self.length = compute_length(s)
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def operation(self):
            return self.value

    def get_length(self):
        self.length = self.nested.operation()
        return self.length


str_len = Len("Hello, World!")
str_len.nested.value = "World"
result = str_len.get_length()
