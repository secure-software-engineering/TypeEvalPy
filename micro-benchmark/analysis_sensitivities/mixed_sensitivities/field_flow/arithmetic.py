# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# The program is also flow sensitive as the result changes according to values assigned to the member variables a and b in execution flow.


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

arith_op.a = -10
arith_op.b = 5
result = arith_op.compute()
