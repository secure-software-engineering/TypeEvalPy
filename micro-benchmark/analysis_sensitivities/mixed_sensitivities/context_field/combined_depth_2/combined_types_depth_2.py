# A class called CombinedTypesContext is defined that has a member variable 'data' and a nested class called 'Nested'.
# The 'Nested' class also has a member variable 'value'.
# The 'CombinedTypesContext' class is field-sensitive, allowing 'data' and 'Nested.value' to store different types of values in different contexts.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data' or 'Nested.value'.


def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World"
    return x


class ValueStore:
    def __init__(self, a):
        self.a = self.Nested(a)

    class Nested:
        def __init__(self, b):
            self.b = b


op1 = ValueStore(True)
op2 = ValueStore(False)

result1 = my_function(op1.a.b)
result2 = my_function(op2.a.b)
