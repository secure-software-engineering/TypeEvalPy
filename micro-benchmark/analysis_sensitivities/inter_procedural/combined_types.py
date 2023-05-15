# A program that defines a function called 'my_function' with combined return types.
# The function is called from another function 'operation' which takes a boolean parameter and returns the value returned by 'my_function'.


def my_function(my_bool):
    if my_bool:
        return 5
    else:
        return "Hello World!"


def operation(my_bool):
    result = my_function(my_bool)
    return result


result = operation(True)
