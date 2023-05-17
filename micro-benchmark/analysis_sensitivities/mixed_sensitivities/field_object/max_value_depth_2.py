# A class called MaxValueObject is defined that has member variables 'a', 'b', and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'MaxValueObject' class is field-sensitive, allowing 'a', 'b', and 'Nested.value' to store different types of values in different objects.
# The class has a method called 'get_max_value' which returns the maximum value between 'a', 'b', and 'Nested.value'.


class MaxValueObject:
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


object1 = MaxValueObject(5, 10)
object2 = MaxValueObject(3, 2)
object2.nested.value = object1.nested.value
result1 = object1.get_max_value()
result2 = object2.get_max_value()
