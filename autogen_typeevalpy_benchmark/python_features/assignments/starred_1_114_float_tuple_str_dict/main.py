# Functions are assigned to variables via starred assignment
def func1():
    return 86.61


def func2():
    return (17, 1, 25)


def func3():
    return 'igcyt'


def func4():
    return {'rxfnq': 13, 'vznts': 27, 'wkywm': 12}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
