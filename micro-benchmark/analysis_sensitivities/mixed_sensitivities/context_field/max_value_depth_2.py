# A class called MaxValueContext is defined that has member variables 'a', 'b', and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'MaxValueContext' class is field-sensitive, allowing 'a', 'b', and 'Nested.value' to store different types of values in different contexts.
# The class has a method called 'get_max_value' which returns the maximum value between 'a', 'b', and 'Nested.value'.


class MaxValueContext:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    def get_max_value(self):
        max_value = max(self.a, self.b)
        nested_value = self.nested.get_value()
        if isinstance(max_value, int) and isinstance(nested_value, int):
            return max(max_value, nested_value)
        else:
            return None


context1 = MaxValueContext(5, 10)
context2 = MaxValueContext(3, 2)
context2.nested.value = 20.1
result1 = context1.get_max_value()
result2 = context2.get_max_value()
