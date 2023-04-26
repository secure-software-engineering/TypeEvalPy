# Program defines a class called 'ArithmeticOperation'.
# The class takes two parameters 'a' and 'b' in its constructor, and has a method called 'compute' that computes the sum of the two parameters.
# The class also has a member variable 'result' that stores the result of the computation.
# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        self.result = self.a + self.b
        return self.result


arith_op = ArithmeticOperation(5, 10)
arith_op.a = "Hello"
arith_op.b = "world"
result = arith_op.compute()
