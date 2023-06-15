# A Python program that defines a function called 'identity' which will simply return the type of  variable
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def identity(x):
    return type(x)


result1 = identity(5)
result2 = identity(5.2)
result3 = identity("Hello")
result4 = identity([1, 2, 3])
