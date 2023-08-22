# This program is an example of context sensitivity as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'a' and 'b' fields of the 'ArithmeticOperation' class objects.
# It is also an example of field sensitivity because the 'compute' method of the 'ArithmeticOperation' class is dependent on the values of the 'a' and 'b' fields of the object on which it is called.
# Also it has multiple depth in field sensitivity


def arithmetic_op(a, b):
    result = a + b
    return result


class ValueStore:
    def __init__(self, a, b):
        self.a = a
        self.b = self.Nested(b)

    class Nested:
        def __init__(self, b):
            self.b = b


op1 = ValueStore(5, 10)
op2 = ValueStore("Hello", "World")

result1 = arithmetic_op(op1.a, op1.b.b)
result2 = arithmetic_op(op2.a, op2.b.b)
