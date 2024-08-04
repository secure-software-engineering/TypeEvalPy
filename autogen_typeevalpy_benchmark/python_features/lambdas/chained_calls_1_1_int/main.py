# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(6)


def func2(a, b):
    a(6)
    return func3(b)


def func1(a, b, c):
    a(6)
    return func2(b, c)


d = func1(lambda x: x + 6, lambda x: x + 6, lambda x: x + 6)
