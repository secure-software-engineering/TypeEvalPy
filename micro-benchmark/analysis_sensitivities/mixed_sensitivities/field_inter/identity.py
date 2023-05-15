# This is field-sensitive , allowing the value member variable to store different types of values in different contexts.
# The given code is interprocedural because it involves calling a separate function operation


class Identity:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        return self.operation()

    def operation(self):
        return str(self.value) + " string"


id1 = Identity(5)
id1.value = "Hello"
result = id1.get_value()
