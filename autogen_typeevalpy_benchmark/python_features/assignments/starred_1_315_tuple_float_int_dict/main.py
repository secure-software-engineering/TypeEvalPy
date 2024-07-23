# Functions are assigned to variables via starred assignment
def func1():
    return (42, 82, 19)


def func2():
    return 82.26


def func3():
    return 1


def func4():
    return {'qbgjq': 3, 'kicjy': 36, 'ttxib': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
