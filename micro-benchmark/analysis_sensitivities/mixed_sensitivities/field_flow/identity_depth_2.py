# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# Also it has multiple depth in field sensitivity


class Identity:
    def __init__(self, x):
        self.nested = self.Nested(x)

    class Nested:
        def __init__(self, y):
            self.value = y

    def get_value(self):
        if isinstance(self.nested.value, str):
            return self.nested.value * 3
        elif isinstance(self.nested.value, int):
            return self.nested.value + 1
        else:
            return None


id1 = Identity(5)
result = id1.get_value()

id2 = Identity("Hello")
result = id2.get_value()

id2.nested.value = 20.0
result = id2.get_value()
