# Functions are assigned to variables via starred assignment
def func1():
    return {'tnaiz': 49, 'tsdcz': 10, 'bckxs': 34}


def func2():
    return (33, 36, 49)


def func3():
    return 'fsijm'


def func4():
    return 50

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
