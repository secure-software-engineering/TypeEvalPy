# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# The program is also flow sensitive as the result changes according to values assigned to the member variables a and b in execution flow.
class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def change_value(self, u, v):
        self.a = u
        self.b = v

    def compute(self):
        self.result = self.a + self.b
        return self.result


x = 5
y = 10
arith_op = ArithmeticOperation(x, y)
arith_op.a = "Hello"
arith_op.b = "world"
result = arith_op.compute()
x = 10
y = 5
arith_op.change_value(x, y)
result2 = arith_op.compute()
