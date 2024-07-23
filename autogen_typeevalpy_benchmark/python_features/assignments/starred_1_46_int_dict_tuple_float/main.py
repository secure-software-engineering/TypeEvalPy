# Functions are assigned to variables via starred assignment
def func1():
    return 20


def func2():
    return {'owkxf': 68, 'wfleg': 5, 'cmhnz': 41}


def func3():
    return (14, 36, 49)


def func4():
    return 17.74

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
