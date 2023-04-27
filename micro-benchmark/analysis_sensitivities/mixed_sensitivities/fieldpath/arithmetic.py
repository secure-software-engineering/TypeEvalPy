# The modified program is path-sensitive because it has different execution paths depending on the values of the inputs a and b.
# The modified program is also field-sensitive because it modifies the state of the object arith_op by assigning new values to its fields a and b
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

        if self.result is not None and self.result < 0:
            self.result = None
        elif self.result is not None:
            self.result = "Positive"

        return self.result


arith_op = ArithmeticOperation(5, 10)
result = arith_op.compute()
