# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(67.71)


def func2(a, b):
    a(67.71)
    return func3(b)


def func1(a, b, c):
    a(67.71)
    return func2(b, c)


d = func1(lambda x: x + 67.71, lambda x: x + 67.71, lambda x: x + 67.71)
