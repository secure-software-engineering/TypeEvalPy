# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a('rzulo')


def func2(a, b):
    a('rzulo')
    return func3(b)


def func1(a, b, c):
    a('rzulo')
    return func2(b, c)


d = func1(lambda x: x + 'rzulo', lambda x: x + 'rzulo', lambda x: x + 'rzulo')
