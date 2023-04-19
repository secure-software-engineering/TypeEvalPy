# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(1)


def func2(a, b):
    a(1)
    return func3(b)


def func1(a, b, c):
    a(1)
    return func2(b, c)


d = func1(lambda x: x + 1, lambda x: x + 2, lambda x: x + 3)
