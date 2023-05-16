# A program that defines a class called `LenOperation` which takes one parameter `value` in its constructor and has a method called `calculate_length` which returns the length of the `value` attribute.
# The behavior of the `calculate_length` method is object-sensitive as it depends on the type and value of the `value` attribute of the instance.


class LenOperation:
    def __init__(self, value):
        self.value = value

    def calculate_length(self):
        if isinstance(self.value, str):
            return len(self.value)
        elif isinstance(self.value, list):
            return len(self.value)
        else:
            return None


text = "Hello World"
numbers = [1, 2, 3, 4, 5]
len_op1 = LenOperation(text)
len_op2 = LenOperation(numbers)
result1 = len_op1.calculate_length()
result2 = len_op2.calculate_length()
