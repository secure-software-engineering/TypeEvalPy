# A program that defines a function called 'max_value' which returns the maximum value among the input parameters.
# The function is called from another function 'operation' which takes two parameters and returns the maximum value among their identities.


def max_value(a, b):
    return max(a, b)


def operation(a, b):
    result = max_value(a, b)
    return result


result = operation(5, 10)
