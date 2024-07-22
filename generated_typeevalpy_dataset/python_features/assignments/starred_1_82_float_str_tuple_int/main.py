# Functions are assigned to variables via starred assignment
def func1():
    return 47.76


def func2():
    return 'egpxz'


def func3():
    return (33, 67, 61)


def func4():
    return 78

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
