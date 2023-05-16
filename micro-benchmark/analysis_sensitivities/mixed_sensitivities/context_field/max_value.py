# A class called MaxValueContext is defined that stores two values in member variables 'a' and 'b'.
# The class has a method called 'get_max_value' which returns the maximum value between 'a' and 'b'.
# The 'a' and 'b' member variables are field-sensitive, allowing them to store different types of values in different contexts.


class MaxValueContext:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_max_value(self):
        return max(self.a, self.b)


context1 = MaxValueContext(5, 10)
context2 = MaxValueContext("Hello", "World")
context2.b = "Context"
result1 = context1.get_max_value()
result2 = context2.get_max_value()
