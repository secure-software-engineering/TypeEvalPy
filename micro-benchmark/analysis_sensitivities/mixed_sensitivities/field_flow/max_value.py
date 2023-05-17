# A class MaxValue is defined that compares two values and stores the maximum value in a field-sensitive member variable 'max_value'.
# The constructor takes two values as parameters, and the get_max_value method returns the maximum value.
# The field sensitivity allows the 'max_value' member variable to store different values in different contexts.
# Flow sensitive as it takes different path depending on values.


class MaxValue:
    def __init__(self, a, b):
        self.max_value = max(a, b)

    def get_max_value(self):
        if isinstance(self.max_value, int):
            return self.max_value
        else:
            return None


max_val = MaxValue(5, 10)
max_val2 = MaxValue(5, 15)
max_val2.max_value = "Hello"
result = max_val.get_max_value()
result2 = max_val2.get_max_value()
