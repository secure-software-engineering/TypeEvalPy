# Program is flow and object sensitive as different objects are used which should be recognised and value of one object changes during the flow of program.


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
arith_op1.a = "Hello"
arith_op1.b = "World"
result2 = arith_op1.compute()
