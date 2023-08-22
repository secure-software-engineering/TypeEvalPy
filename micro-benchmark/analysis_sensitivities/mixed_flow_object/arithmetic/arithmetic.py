# Program is flow and object sensitive as different objects are used which should be recognised and value of one object changes during the flow of program.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        if self.a == 0:
            self.result = self.b
        elif self.b == 0:
            self.result = self.a
        else:
            self.result = self.a + self.b
        return self.result


arith_op = ArithmeticOperation(5, 10)
result = arith_op.compute()

arith_op = ArithmeticOperation(5, 0)
result = arith_op.compute()

arith_op = ArithmeticOperation(0, 10)
result = arith_op.compute()

arith_op = ArithmeticOperation("Hello", "World")
result = arith_op.compute()
