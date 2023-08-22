# A class called CombinedTypes is defined that has a member variable 'data' and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'CombinedTypes' class is field-sensitive, allowing 'data' and 'Nested.value' to store different types of values in different contexts.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data' or 'Nested.value'.


class CombinedTypes:
    def __init__(self, data):
        self.nested = self.Nested(data)

    class Nested:
        def __init__(self, value):
            self.value = value

    def process_data(self):
        if isinstance(self.nested.value, int):
            return self.nested.value * 2
        elif isinstance(self.nested.value, str):
            return self.nested.value * 3
        else:
            return self.nested.value


context1 = CombinedTypes(5)
result = context1.process_data()

context2 = CombinedTypes("hello")
result = context2.process_data()

context2.nested.value = 20
result = context2.process_data()
