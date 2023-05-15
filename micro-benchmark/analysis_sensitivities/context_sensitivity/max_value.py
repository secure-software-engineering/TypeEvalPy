# A simple Python program that defines a function called 'max_value' which return the maximum value in parameters.
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def max_value(a, b):
    return max(a, b)


a = "Hello"
b = "world!"
result = max_value(a, b)
a = [1, 1]
b = [1, 2, 3]
result = max_value(a, b)
