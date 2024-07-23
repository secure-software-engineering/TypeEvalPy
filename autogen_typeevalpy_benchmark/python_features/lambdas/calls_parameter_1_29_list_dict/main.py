# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [54, 2, 37]


def func2():
    return {'hglyn': 24, 'yqwwk': 18, 'diqlg': 27}


x = lambda x: x()

a = x(func1)

b = x(func2)
