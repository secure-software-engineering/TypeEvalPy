# A class Len is defined that computes the length of a string and stores it in a field-sensitive member variable 'length'.
# The constructor takes a string as a parameter, and the get_length method returns the length of the string.
# The field sensitivity allows the 'length' member variable to store different values in different contexts.
# Flow sensitive as it takes different path depending on values.


class Len:
    def __init__(self, s):
        self.length = len(s)

    def get_length(self):
        if isinstance(self.length, int):
            return self.length
        else:
            return None


str_len = Len("Hello, World!")
str_len2 = Len([1, 2, 3])
result = str_len.get_length()
str_len2.length = 3.5
result2 = str_len2.get_length()
