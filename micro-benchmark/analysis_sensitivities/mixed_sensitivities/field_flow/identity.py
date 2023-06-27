# A class Identity is defined that can store different types of values in a member variable value.
# The constructor takes an initial value as a parameter, and the get_value method returns the current value of self.valuethe value member variable.
# This is field-sensitive , allowing the value member variable to store different types of values in different contexts.
# Also it is flow sensitive as it chooses different path of flow depending on value.


class Identity:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        if isinstance(self.value, str):
            return self.value * 3
        elif isinstance(self.value, int):
            return self.value + 1
        else:
            return None


id1 = Identity(5)
result = id1.get_value()

id2 = Identity("Hello")
result = id2.get_value()

id2.value = 6.0
result = id2.get_value()
