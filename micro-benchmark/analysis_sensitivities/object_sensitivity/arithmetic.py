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
