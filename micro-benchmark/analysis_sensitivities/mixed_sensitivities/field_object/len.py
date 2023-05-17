# A class Len is defined that computes the length of a string and stores it in a field-sensitive member variable 'length'.
# The constructor takes a string as a parameter, and the get_length method returns the length of the string.
# The behavior of the get_length method depends on the type of the 's' attribute of the instance.
# This is object sensitive and field sensitive, allowing the 'length' member variable to store different values in different contexts.


class Len:
    def __init__(self, s):
        self.s = s
        self.length = None

    def get_length(self):
        self.length = len(self.s)
        return self.length


str_len = Len("Hello, World!")
result = str_len.get_length()
str_len2 = Len([1, 2, 3])
str_len2.s = str_len.s
result2 = str_len2.get_length()
