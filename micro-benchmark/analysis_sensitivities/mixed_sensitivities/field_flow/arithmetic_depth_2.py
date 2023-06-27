# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# The program is also flow sensitive as the result changes according to values assigned to the member variables a and b in execution flow.
# Also it has multiple depth in field sensitivity


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.result = None
        self.nested = self.Nested(b)

    class Nested:
        def __init__(self, b):
            self.b = b

    def compute(self):
        self.b = self.nested.b
        if self.a == 0:
            self.result = 0
        elif self.b == 0:
            self.result = 0
        else:
            self.result = self.a + self.b

        if self.result is not None and self.result <= 0:
            self.result = None
        elif self.result is not None:
            self.result = "Positive"

        return self.result


arith_op = ArithmeticOperation(5, 10)
result = arith_op.compute()

arith_op.a = 0
arith_op.nested.b = -5
result = arith_op.compute()
