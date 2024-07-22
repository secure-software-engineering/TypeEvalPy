# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return [90, 93, 30]


def func3():
    return {'nrkhp': 49, 'rbnqv': 44, 'cbdcb': 87}


def func4():
    return (81, 28, 54)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
