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
