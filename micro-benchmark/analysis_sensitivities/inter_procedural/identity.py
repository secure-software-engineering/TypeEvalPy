# Program defines a function called 'identity' which returns the input variable as it is.
# The function is called from another function 'operation' which takes two parameters and returns the sum of their identities.


def identity(x):
    return x


def operation(a, b):
    result = identity(a) + identity(b)
    return result


result = operation(5, 10)
