# Program defines a function called 'identity' which returns the input variable as it is.
# The function is called from another function 'operation' which takes two parameters and returns the sum of their identities.


def identity(x):
    return x


def operation(a):
    result = identity(a)
    return result


result1 = operation(5)
result2 = operation(5.0)
result3 = operation("Hello world")