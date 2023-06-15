# A class called CombinedTypes is defined that stores a value in a member variable 'data'.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data'.
# The 'data' member variable is field-sensitive, allowing it to store different types of values in different contexts.


class CombinedTypes:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        if isinstance(self.data, int):
            return self.data * 2
        elif isinstance(self.data, str):
            return self.data * 3
        else:
            return self.data


context1 = CombinedTypes(5)
result = context1.process_data()

context2 = CombinedTypes("hello")
result = context2.process_data()

context2.data = [1, 2]
result = context2.process_data()
