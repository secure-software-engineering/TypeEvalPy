# A program that defines a class called `CombinedTypesOperation` which takes one parameter `value' in its constructor and has a method called combined_types which performs different operations on thevalue` attribute based on its type.
# The behavior of the combined_types method is object-sensitive as it depends on the type and value of the value attribute of the instance.
class CombinedTypesOperation:
    def __init__(self, value):
        self.value = value


def combined_types(self):
    if isinstance(self.value, int):
        return self.value * 2
    elif isinstance(self.value, str):
        return self.value.upper()
    else:
        return None


value1 = 5
value2 = 2.5
combined_op1 = CombinedTypesOperation(value1)
combined_op2 = CombinedTypesOperation(value2)
result1 = combined_op1.combined_types()
result2 = combined_op2.combined_types()
