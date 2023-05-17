# A class Len is defined that computes the length of a string and stores it in a field-sensitive member variable 'length'.
# The constructor takes a string as a parameter, and the get_length method returns the length of the string.
# The field sensitivity allows the 'length' member variable to store different values in different contexts.
# The code involves calling a separate function 'compute_length' to perform the length computation.


def compute_length(s):
    return len(s)


class Len:
    def __init__(self, s):
        self.length = s

    def get_length(self):
        self.length = compute_length(self.s)
        if isinstance(self.length, int):
            return self.length
        else:
            return None


str_len = Len("Hello, World!")
str_len.s = [1, 2, 3]
result = str_len.get_length()
