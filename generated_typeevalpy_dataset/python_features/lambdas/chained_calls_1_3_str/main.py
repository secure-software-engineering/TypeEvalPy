# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a('oesnp')


def func2(a, b):
    a('oesnp')
    return func3(b)


def func1(a, b, c):
    a('oesnp')
    return func2(b, c)


d = func1(lambda x: x + 'oesnp', lambda x: x + 'oesnp', lambda x: x + 'oesnp')
