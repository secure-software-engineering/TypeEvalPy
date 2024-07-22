# Functions are assigned to variables via starred assignment
def func1():
    return {'nqjup': 75, 'ioesx': 36, 'fwhyh': 74}


def func2():
    return [71, 21, 78]


def func3():
    return 56.53


def func4():
    return 'agpmr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
