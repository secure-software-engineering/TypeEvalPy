# Functions are assigned to variables via starred assignment
def func1():
    return {'ifpxs': 34, 'txffs': 4, 'qswaq': 100}


def func2():
    return (60, 93, 90)


def func3():
    return 54.75


def func4():
    return 'dlspl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
