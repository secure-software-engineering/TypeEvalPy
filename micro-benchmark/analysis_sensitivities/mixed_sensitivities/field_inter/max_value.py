# A class MaxValue is defined that compares two values and stores the maximum value in a field-sensitive member variable 'max_value'.
# The constructor takes two values as parameters, and the get_max_value method returns the maximum value.
# The field sensitivity allows the 'max_value' member variable to store different values in different contexts.
# The code involves calling a separate function 'max_value' to determine the maximum value.


def max_value(a, b):
    return max(a, b)


class MaxValue:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.max_value = max_value(self.a, self.b)

    def get_max_value(self):
        if isinstance(self.max_value, int):
            return self.max_value
        else:
            return None


max_val = MaxValue(5, 10)
max_val.max_value = "Hello"
result = max_val.get_max_value()
