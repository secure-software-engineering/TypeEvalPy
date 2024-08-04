# Functions are assigned to variables via starred assignment
def func1():
    return {'qcrmy': 20, 'cxqfr': 25, 'qanfp': 26}


def func2():
    return 71.83


def func3():
    return (65, 42, 37)


def func4():
    return 'axkpi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
