# This program is an example of context sensitivity as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'a' and 'b' fields of the 'ArithmeticOperation' class objects.
# It is also an example of field sensitivity because the 'compute' method of the 'ArithmeticOperation' class is dependent on the values of the 'a' and 'b' fields of the object on which it is called.
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
            return self.b

    def compute(self):
        self.result = self.a + self.nested.compute()
        return self.result


result1 = ArithmeticOperation(5, 10)
first_result = result1.compute()
result2 = ArithmeticOperation("Hello", "World")
final_result = result2.compute()
