# Functions are assigned to variables via starred assignment
def func1():
    return 'mlupy'


def func2():
    return (75, 92, 39)


def func3():
    return 62


def func4():
    return {'kdcmz': 50, 'mhlht': 88, 'klnud': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
