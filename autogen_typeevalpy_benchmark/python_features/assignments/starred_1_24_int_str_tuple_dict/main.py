# Functions are assigned to variables via starred assignment
def func1():
    return 43


def func2():
    return 'xcthm'


def func3():
    return (48, 28, 57)


def func4():
    return {'tmfjg': 17, 'axogt': 86, 'qfvfl': 30}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
