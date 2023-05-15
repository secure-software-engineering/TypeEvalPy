# The given code is an example of field sensitivity because it can recognise values based on the values assigned to its member variables.
# Program is interprocedural as it calls another fucntion operation from get_value
# Also it has multiple depth in field sensitivity
class Identity:
    def __init__(self, x):
        self.value = x
        self.nested = self.Nested(self.value)

    class Nested:
        def __init__(self, y):
            self.value = y

        def operation(self):
            return str(self.value) + " string"

    def get_value(self):
        return self.nested.operation()


id1 = Identity(5)
id2 = Identity("Hello")

id2.nested.value = 20

result1 = id1.get_value()
result2 = id2.get_value()
