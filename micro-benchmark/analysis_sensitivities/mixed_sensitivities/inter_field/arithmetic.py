# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also field sensitive as it can recognise values based on the values assigned to its member variables.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        self.result = self.add(self.a, self.b)
        return self.result

    def add(self):
        self.result = self.a + self.b
        return self.result


arith_op = ArithmeticOperation(5, 10)
arith_op.a = "Hello"
arith_op.b = "world"
result = arith_op.compute()
