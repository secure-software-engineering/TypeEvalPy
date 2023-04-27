# This program is an example of flow sensitivity as the behavior of the program is dependent on the flow of execution, specifically the values assigned to the 'a' and 'b' fields of the 'arith_op' object.
# It is also an example of field sensitivity because the 'compute' method of the 'ArithmeticOperation' class is dependent on the values of the 'a' and 'b' fields of the object on which it is called.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        self.result = self.a + self.b
        return self.result


arith_op = ArithmeticOperation(5, 10)
arith_op.a = "Hello"
arith_op.b = "world"
result = arith_op.compute()
