# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# It is also object and field sensitive as field of different objects (eg: arith_op1.a = arith_op2.a) should be identified for successful execution.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.result = None
        self.nested = self.Nested(b)

    class Nested:
        def __init__(self, b):
            self.b = b

        def compute(self):
            return self.b

    def compute(self):
        self.b = self.nested.compute()
        self.result = self.a + self.b
        return self.result


arith_op1 = ArithmeticOperation(5, 10)
arith_op2 = ArithmeticOperation("Hello", "World")
result1 = arith_op1.compute()
arith_op1.a = arith_op2.a
arith_op1.nested.b = arith_op2.nested.b
result2 = arith_op1.compute()
