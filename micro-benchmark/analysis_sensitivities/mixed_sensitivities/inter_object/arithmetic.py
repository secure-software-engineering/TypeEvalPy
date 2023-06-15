# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also object sensitive as it has to differentiate between objects


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = 10

    def compute(self):
        self.result = self.add(self.a, self.b)
        return self.result

    def add(self, a, b):
        self.result = a + b
        return self.result


arith_op1 = ArithmeticOperation(5, 10)
arith_op2 = ArithmeticOperation("Hello", "World")

result = arith_op1.compute()
result2 = arith_op2.compute()
