# A class Len is defined that computes the length of a string and stores it in a field-sensitive member variable 'length'.
# The constructor takes a string as a parameter, and the get_length method returns the length of the string.
# The field sensitivity allows the 'length' member variable to store different values in different contexts.
# The code also includes a nested class 'Nested' for multiple depth in field sensitivity.


class Len:
    def __init__(self, s):
        self.length = len(s)
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def get_value(self):
            return self.value

    def get_length(self):
        if isinstance(self.nested.get_value(), int):
            self.length = self.nested.get_value()
        else:
            self.length = None
        return self.length


str_len = Len("Hello, World!")
result = str_len.get_length()
str_len.nested.value = 5.5
result = str_len.get_length()
