# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
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
        self.result = self.a + self.nested.b
        return self.result


arith_op = ArithmeticOperation(5, 4)
result1 = arith_op.compute()
