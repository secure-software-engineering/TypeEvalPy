# Functions are assigned to variables via starred assignment
def func1():
    return 4.05


def func2():
    return [89, 36, 32]


def func3():
    return 'vtapl'


def func4():
    return {'jxcrn': 91, 'rzkhp': 9, 'ocmfo': 25}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
