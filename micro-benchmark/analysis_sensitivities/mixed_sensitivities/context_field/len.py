# A class called Len is defined that stores a value in a member variable 'value'.
# The class has a method called 'compute_length' which returns the length of the 'value' member variable.
# The 'value' member variable is field-sensitive, allowing it to store different types of values in different contexts.


class Len:
    def __init__(self, value):
        self.value = value

    def compute_length(self):
        return len(self.value)


context1 = Len("Hello")
context2 = Len([1, 2, 3, 4, 5])
context2.value = "1234"
result1 = context1.compute_length()
result2 = context2.compute_length()
