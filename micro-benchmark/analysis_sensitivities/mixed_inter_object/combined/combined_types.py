# Program defines a class called CombinedTypesOperation which takes one parameter x in its constructor, and has a method called combined_types that performs different operations on the x attribute based on its type.
# This program is object-sensitive and interprocedural as the behavior of the combined_types method depends on the type and value of the x attribute of the instance, and it calls other functions to perform the operations.


class CombinedTypesOperation:
    def __init__(self, x):
        self.x = x
        self.result = None

    def combined_types(self):
        if isinstance(self.x, int):
            self.result = self.multiply_by_two()
        elif isinstance(self.x, str):
            self.result = self.multiply_string()
        else:
            self.result = None
        return self.result

    def multiply_by_two(self):
        self.result = self.x * 2
        return self.result

    def multiply_string(self):
        self.result = self.x * 3
        return self.result


combined_op1 = CombinedTypesOperation(5)
combined_op2 = CombinedTypesOperation("hello")

result1 = combined_op1.combined_types()
result2 = combined_op2.combined_types()
