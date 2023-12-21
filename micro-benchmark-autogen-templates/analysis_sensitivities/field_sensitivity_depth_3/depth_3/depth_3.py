# Program for field sensitivity analysis in depth 3


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.result = None
        self.nested = self.Nested(b)

    class Nested:
        def __init__(self, b):
            self.nested2 = self.Nested2(b)

        class Nested2:
            def __init__(self, c):
                self.c = c

    def compute(self):
        self.result = self.a + self.nested.nested2.c
        return self.result


arith_op = ArithmeticOperation(<value1>, <value1>)
result1 = arith_op.compute()
