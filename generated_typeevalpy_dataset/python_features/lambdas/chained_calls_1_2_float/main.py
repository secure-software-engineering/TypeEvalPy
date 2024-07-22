# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(69.11)


def func2(a, b):
    a(69.11)
    return func3(b)


def func1(a, b, c):
    a(69.11)
    return func2(b, c)


d = func1(lambda x: x + 69.11, lambda x: x + 69.11, lambda x: x + 69.11)
