# This program is an example of context sensitivity as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'a' and 'b' fields of the 'ArithmeticOperation' class objects.
# It is also an example of field sensitivity because the 'compute' method of the 'ArithmeticOperation' class is dependent on the values of the 'a' and 'b' fields of the object on which it is called.


class ArithmeticOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def compute(self):
        self.result = self.a + self.b
        if self.result >= 5:
            self.result = 0
        else:
            self.result = "Negative"
        return self.result


x = 2
y = 1
result1 = ArithmeticOperation(x, y)
first_result = result1.compute()
u = 3
v = 2
result2 = ArithmeticOperation(u, v)
final_result = result2.compute()
