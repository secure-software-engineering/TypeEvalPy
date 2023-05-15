# A class MaxValue is defined that stores two values in member variables value1 and value2.
# The constructor takes two initial values as parameters, assigning them to the respective member variables.
# The get_max method compares value1 and value2 using the max() function and returns the maximum value.
# This is field-sensitive, allowing the value member variable to store different types of values


class MaxValue:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def get_max(self):
        return max(self.value1, self.value2)


mf = MaxValue(10, 20)

result = mf.get_max()
