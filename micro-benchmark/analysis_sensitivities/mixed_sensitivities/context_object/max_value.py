# A program that defines a class called `MaxValueOperation` which takes two parameters `a` and `b` in its constructor, and has a method called `compute_max_value` that returns the maximum value between `a` and `b`.
# The behavior of the program is object-sensitive as the behavior of the `compute_max_value` method depends on the types of the `a` and `b` attributes of the instance.
# The `result` field is accessed and modified in a context-sensitive manner, where the behavior of the program depends on the specific context object that is used.


class MaxValueOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute_max_value(self):
        self.result = max(self.a, self.b)
        return self.result


value1 = 5
value2 = 10
max_op1 = MaxValueOperation(value1, value2)
result1 = max_op1.compute_max_value()
max_op2 = MaxValueOperation("value1", "value2")
result2 = max_op2.compute_max_value()
