# Functions are assigned to variables via starred assignment
def func1():
    return 43


def func2():
    return {'smlhh': 32, 'gxyap': 17, 'rcsmj': 89}


def func3():
    return (86, 14, 28)


def func4():
    return 'floro'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
