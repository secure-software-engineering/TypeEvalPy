# A class called MaxValueObject is defined that stores two values in member variables 'a' and 'b'.
# The class has a method called 'get_max_value' which returns the maximum value between 'a' and 'b'.
# The 'a' and 'b' member variables are field-sensitive, allowing them to store different types of values in different objects.


class MaxValueObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_max_value(self):
        return max(self.a, self.b)


object1 = MaxValueObject(5, 10)
object2 = MaxValueObject("Hello", "World")
object2.b = object1.b
result1 = object1.get_max_value()
result2 = object2.get_max_value()
