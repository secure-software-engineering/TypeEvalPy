# A class Identity is defined that can store different types of values in a member variable value.
# The constructor takes an initial value as a parameter, and the get_value method returns the current value of the value member variable.
# This is field-sensitive, allowing the value member variable to store different types of values


class Len:
    def __init__(self, x):
        self.value = x

    def get_length(self):
        return len(self.value)


lf = Len("Hello, World!")

result = lf.get_length()
