# A class called MaxValueOperation is defined that takes two parameters a and b in its constructor and has a method called max_value that returns the maximum value between a and b.
# The class also has a member variable called result that stores the result of the computation.


class MaxValueOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def max_value(self):
        self.result = max(self.a, self.b)
        return self.result


max_op1 = MaxValueOperation(5, 10)
max_op2 = MaxValueOperation(3.5, 2.8)
result1 = max_op1.max_value()
result2 = max_op2.max_value()
