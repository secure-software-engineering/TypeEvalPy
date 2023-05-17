# A class called CombinedTypes is defined that has a member variable 'data' and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'CombinedTypes' class is field-sensitive, allowing 'data' and 'Nested.value' to store different types of values in different contexts.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data' or 'Nested.value'.


class CombinedTypes:
    def __init__(self, data):
        self.data = data
        self.nested = self.Nested(10)

    class Nested:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    def process_data(self):
        if isinstance(self.data, int):
            return self.data * 2
        elif isinstance(self.nested.value, str):
            return self.nested.value.upper()
        else:
            return self.data


context1 = CombinedTypes(5)
context2 = CombinedTypes("hello")
context2.nested.value = 20
result1 = context1.process_data()
result2 = context2.process_data()
