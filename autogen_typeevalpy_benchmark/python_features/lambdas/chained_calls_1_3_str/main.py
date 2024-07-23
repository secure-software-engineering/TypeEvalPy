# Lambdas are passed via parameters to chained functions and then called.


def func3(a):
    return a('gqpkj')


def func2(a, b):
    a('gqpkj')
    return func3(b)


def func1(a, b, c):
    a('gqpkj')
    return func2(b, c)


d = func1(lambda x: x + 'gqpkj', lambda x: x + 'gqpkj', lambda x: x + 'gqpkj')
