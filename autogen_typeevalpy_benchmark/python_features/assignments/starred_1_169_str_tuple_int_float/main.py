# Functions are assigned to variables via starred assignment
def func1():
    return 'tygqs'


def func2():
    return (60, 78, 28)


def func3():
    return 99


def func4():
    return 98.9

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
