# Functions are assigned to variables via starred assignment
def func1():
    return {'unuat': 90, 'mvluw': 43, 'ixezf': 89}


def func2():
    return 77.05


def func3():
    return 85


def func4():
    return (94, 47, 77)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
