# A class CombinedTypes is defined that has a field-sensitive member variable 'x'.
# The constructor takes a boolean parameter and assigns different values to 'x' based on the boolean value.
# The get_value method returns 'x', which can have a combined return type of [int, str].
# The field sensitivity allows 'x' to store different types of values in different contexts.
# The object sensitivity enables to differentiate between objects.


class CombinedTypes:
    def __init__(self, my_bool):
        if my_bool:
            self.x = 5
        else:
            self.x = "Hello World!"

    def get_value(self):
        if isinstance(self.x, int):
            return self.x + 1
        else:
            return self.x * 3


obj1 = CombinedTypes(True)
obj2 = CombinedTypes(False)

result1 = obj1.get_value()
result2 = obj2.get_value()

obj2.x = obj1.x
result3 = obj2.get_value()
