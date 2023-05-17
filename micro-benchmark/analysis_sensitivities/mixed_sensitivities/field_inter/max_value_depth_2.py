# A class MaxValue is defined that compares two values and stores the maximum value in a field-sensitive member variable 'max_value'.
# The constructor takes two values as parameters, and the get_max_value method returns the maximum value.
# The field sensitivity allows the 'max_value' member variable to store different values in different contexts.
# The code involves calling a separate function 'max_value' to determine the maximum value.
# The code also includes a nested class 'Nested' to demonstrate multiple depth in field sensitivity.


def max_value(a, b):
    return max(a, b)


class MaxValue:
    def __init__(self, a, b):
        self.max_value = max_value(a, b)
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def operation(self):
            return self.value

    def get_max_value(self):
        if isinstance(self.nested.operation(), int):
            self.max_value = max(self.max_value, self.nested.operation())
        else:
            self.max_value = self.nested.operation()
        return self.max_value


max_val = MaxValue(5, 100)
max_val.nested.value = 20.1
result = max_val.get_max_value()
