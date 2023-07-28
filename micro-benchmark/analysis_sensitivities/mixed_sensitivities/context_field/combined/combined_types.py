# A class called CombinedTypesContext is defined that stores a value in a member variable 'data'.
# The class has a method called 'process_data' which returns the processed data based on the type of 'data'.
# The 'data' member variable is field-sensitive, allowing it to store different types of values in different contexts.


def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World"
    return x


class ValueStore:
    def __init__(self, a):
        self.a = a


op1 = ValueStore(True)
op2 = ValueStore(False)

result1 = my_function(op1.a)
result2 = my_function(op2.a)
