# A Python program that defines a function called 'my_function' with combined return types.
# The given code is flow-sensitive because it produces different results based on the flow of the program execution.


def my_function(my_bool):
    if my_bool:
        return 5
    else:
        return "Hello World!"


result1 = my_function(True)
result2 = my_function(False)
result3 = my_function(0)
