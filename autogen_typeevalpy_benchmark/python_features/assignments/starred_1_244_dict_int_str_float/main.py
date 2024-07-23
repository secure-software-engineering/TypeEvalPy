# Functions are assigned to variables via starred assignment
def func1():
    return {'umjpp': 37, 'ogkcq': 95, 'lrysa': 26}


def func2():
    return 3


def func3():
    return 'djtca'


def func4():
    return 40.06

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
