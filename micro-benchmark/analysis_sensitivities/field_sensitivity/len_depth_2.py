# The given code is an example of field sensitivity because it can recognize values based on the values assigned to its member variables.
# It also demonstrates multiple levels of field sensitivity.
class Len:
    def __init__(self, x):
        self.value = x
        self.nested = self.Nested("Nested")

    class Nested:
        def __init__(self, y):
            self.value = y

        def get_length(self):
            return len(self.value)

    def get_length(self):
        return self.nested.get_length()


lf = Len("Hello, World!")
lf.nested.value = "New value"

result = lf.get_length()
