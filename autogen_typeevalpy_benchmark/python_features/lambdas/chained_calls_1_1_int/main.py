# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(50)


def func2(a, b):
    a(50)
    return func3(b)


def func1(a, b, c):
    a(50)
    return func2(b, c)


d = func1(lambda x: x + 50, lambda x: x + 50, lambda x: x + 50)
