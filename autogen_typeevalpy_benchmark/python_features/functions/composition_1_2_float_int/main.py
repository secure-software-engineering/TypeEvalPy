# Assigning the result of a function call to a variable, and passing that variable as an argument to another function.


def add(x, y):
    return x + y


def square(x):
    return x * x


a = square(add(4.97, 4.97))
b = square(add(36, 36))
