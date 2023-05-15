808  # The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.


# Also it has multiple depth in field sensitivity
class Identity:
    def __init__(self, x):
        self.value = x
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, y):
            self.value = y

        def get_value(self):
            return self.value

    def get_value(self):
        return self.nested.get_value()


id1 = Identity(5)
id2 = Identity("Hello")

id2.nested.value = 20

result1 = id1.get_value()
result2 = id2.get_value()
