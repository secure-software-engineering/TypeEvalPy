# A class CombinedTypes is defined that has a field-sensitive member variable 'x'.
# The constructor takes a boolean parameter and assigns different values to 'x' based on the boolean value.
# The get_value method returns 'x', which can have a combined return type of [int, str].
# The field sensitivity allows 'x' to store different types of values in different contexts.
# The code involves calling a separate function 'my_function' to perform the decision.
# The code also includes a nested class 'Nested' to demonstrate multiple depth in field sensitivity.


def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World!"
    return x


class CombinedTypes:
    def __init__(self, my_bool):
        self.x = my_function(my_bool)
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def operation(self):
            return self.value

    def get_value(self):
        if isinstance(self.nested.operation(), str):
            self.x = self.nested.operation().upper()
        return self.x


obj = CombinedTypes(True)
obj.nested.value = "Hello"
result = obj.get_value()
