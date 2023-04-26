# The program defines a class called 'ArithmeticOperation', which has a method called 'compute' that adds two attributes 'a' and 'b' of the class instance, and stores the result in another attribute called 'result'.
# The program creates two instances of the class with different types for the 'a' and 'b' attributes, and calls the 'compute' method on each instance, producing different results.
# This program is an example of object sensitivity.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        self.result = self.a + self.b
        return self.result


arith_op1 = ArithmeticOperation(5, 10)
arith_op2 = ArithmeticOperation("Hello", "World")
result1 = arith_op1.compute()
result2 = arith_op2.compute()
