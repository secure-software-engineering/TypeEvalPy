# Assigning the result of a function call to a variable, and passing that variable as an argument to another function.


def add(x, y):
    return x + y


def square(x):
    return x * x


a = square(add(<value1>, <value1>))
b = square(add(<value2>, <value2>))
