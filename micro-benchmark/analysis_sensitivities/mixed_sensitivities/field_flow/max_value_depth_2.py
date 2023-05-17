# A class MaxValue is defined that compares two values and stores the maximum value in a field-sensitive member variable 'max_value'.
# The constructor takes two values as parameters, and the get_max_value method returns the maximum value.
# The field sensitivity allows the 'max_value' member variable to store different values in different contexts.
# The code also includes a nested class 'Nested' to demonstrate multiple depth in field sensitivity.


class MaxValue:
    def __init__(self, a, b):
        self.max_value = max(a, b)
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def get_value(self):
            return self.value

    def get_max_value(self):
        if isinstance(self.nested.get_value(), int):
            self.max_value = max(self.max_value, self.nested.get_value())
        else:
            self.max_value = None
        return self.max_value


max_val = MaxValue(5, 10)
result = max_val.get_max_value()
max_val.nested.value = "Hello"
result = max_val.get_max_value()
