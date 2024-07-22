# Functions are assigned to variables via starred assignment
def func1():
    return 12


def func2():
    return 'azqpt'


def func3():
    return [35, 3, 39]


def func4():
    return (29, 42, 68)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
