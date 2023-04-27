# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# It is also object and field sensitive as field of different objects (eg: arith_op1.a = arith_op2.a) should be identified for successful execution.


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
arith_op1.a = arith_op2.a
arith_op1.b = arith_op2.b
result2 = arith_op1.compute()
