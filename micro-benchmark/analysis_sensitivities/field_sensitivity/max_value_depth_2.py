# The given code is an example of field sensitivity because it can recognize values based on the values assigned to its member variables.
# It also demonstrates multiple levels of field sensitivity.
class MaxField:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
        self.nested = self.Nested(100, 200)

    class Nested:
        def __init__(self, x, y):
            self.value1 = x
            self.value2 = y

        def get_max(self):
            return max(self.value1, self.value2)

    def get_max(self):
        return self.nested.get_max()


mf = MaxField(10, 20)
mf.nested.value1 = "Hello"
mf.nested.value2 = "World!"
result = mf.get_max()
