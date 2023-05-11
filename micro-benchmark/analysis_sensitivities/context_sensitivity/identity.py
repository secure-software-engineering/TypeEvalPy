# A Python program that defines a function called 'identity' which will simply return the type of  variable
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def identity(x):
    return type(x)


result = identity(5)
result = identity(5.2)
result = identity("Hello")
result = identity([1, 2, 3])
