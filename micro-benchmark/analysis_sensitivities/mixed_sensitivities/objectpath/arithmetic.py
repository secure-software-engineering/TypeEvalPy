# The modified program is path-sensitive because it has different execution paths depending on the values of the inputs a and b.
# The modified program is also object-sensitive because it has to differentiate between objects
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
            self.result = self.add(self.a, self.b)

        if self.result is not None and self.result < 0:
            self.result = None
        elif self.result is not None:
            self.result = "Positive"

        return self.result

    def add(self):
        self.result = self.a + self.b
        return self.result


arith_op1 = ArithmeticOperation(5, 10)
result = arith_op1.compute()
