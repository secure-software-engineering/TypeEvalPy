# A program that defines a class called `LengthOperation` which takes one parameter `data` in its constructor, and has a method called `compute_length` that returns the length of the `data` attribute.
# The behavior of the program is object-sensitive as the behavior of the `compute_length` method depends on the type of the `data` attribute of the instance.
# It is also interprocedural as it calls 2 methods


class LengthOperation:
    def __init__(self, data):
        self.data = data
        self.result = None

    def get_result(self):
        self.compute_length()
        return self.result

    def compute_length(self):
        self.result = len(self.data)


text = "Hello World"
input = [1, 2, 3]
length_op1 = LengthOperation(text)
length_op2 = LengthOperation(input)
result1 = length_op1.get_result()
