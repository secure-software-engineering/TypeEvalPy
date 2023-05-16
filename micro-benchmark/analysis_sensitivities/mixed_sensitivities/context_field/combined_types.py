# A class called CombinedTypesContext is defined that stores a value in a member variable 'data'.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data'.
# The 'data' member variable is field-sensitive, allowing it to store different types of values in different contexts.


class CombinedTypesContext:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        if isinstance(self.data, int):
            return self.data * 2
        elif isinstance(self.data, str):
            return self.data.upper()
        else:
            return self.data


context1 = CombinedTypesContext(5)
context2 = CombinedTypesContext("hello")
context2.data = [1, 2]
result1 = context1.process_data()
result2 = context2.process_data()
