# A program that defines a class called `CombinedTypesOperation which takes one parameterdatain its constructor, and has a method called process_data that performs different operations on thedata` attribute based on its type.


# The behavior of the program is object-sensitive as the behavior of the process_data method depends on the type of the data attribute of the instance.
# The result field is accessed and modified in a context-sensitive manner, where the behavior of the program depends on the specific context object that is used.
class CombinedTypesOperation:
    def __init__(self, data):
        self.data = data
        self.result = None

    def process_data(self):
        if isinstance(self.data, int):
            self.result = self.data * 2
        elif isinstance(self.data, str):
            self.result = self.data.upper()
        else:
            self.result = None
        return self.result


value1 = 5
value2 = 2.5
combined_op1 = CombinedTypesOperation(value1)
combined_op2 = CombinedTypesOperation(value2)
result1 = combined_op1.process_data()
result2 = combined_op2.process_data()
