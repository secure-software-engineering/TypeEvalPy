# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# Also it has multiple depth in field sensitivity
class Identity:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        return self.value


class ValueStore:
    def __init__(self, a):
        self.a = self.Nested(a)

    class Nested:
        def __init__(self, b):
            self.b = b


op1 = ValueStore(5)
op2 = ValueStore("Hello")

id1 = Identity(op1.a.b)
id2 = Identity(op2.a.b)

result1 = id1.get_value()
result2 = id2.get_value()
