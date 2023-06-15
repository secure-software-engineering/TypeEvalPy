# This is field-sensitive , allowing the value member variable to store different types of values in different contexts.
# The given code is interprocedural because it involves calling a separate function operation


class Identity:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        return self.operation()

    def operation(self):
        return self.value


id1 = Identity(5)
result1 = id1.get_value()

id1.value = "Hello"
result2 = id1.get_value()
