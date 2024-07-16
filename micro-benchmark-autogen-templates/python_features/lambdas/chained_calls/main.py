# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a(<value1>)


def func2(a, b):
    a(<value1>)
    return func3(b)


def func1(a, b, c):
    a(<value1>)
    return func2(b, c)


d = func1(lambda x: x + <value1>, lambda x: x + <value1>, lambda x: x + <value1>)
