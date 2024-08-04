# Functions are assigned to variables via starred assignment
def func1():
    return 41.01


def func2():
    return (77, 76, 48)


def func3():
    return 3


def func4():
    return {'nqheg': 69, 'gsoek': 55, 'hahmg': 23}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
