# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also field sensitive as it can recognise values based on the values assigned to its member variables.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.result = None
        self.nested = self.Nested(b)

    class Nested:
        def __init__(self, b):
            self.b = b

    def compute(self):
        self.result = self.add(self.a, self.nested.b)
        return self.result

    def add(self, a, b):
        self.result = a + b
        return self.result


arith_op = ArithmeticOperation(5, 10)
result1 = arith_op.compute()

arith_op.a = "Hello"
arith_op.nested.b = "world"
result2 = arith_op.compute()
