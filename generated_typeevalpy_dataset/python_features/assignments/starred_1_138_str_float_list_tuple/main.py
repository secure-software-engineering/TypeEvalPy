# Functions are assigned to variables via starred assignment
def func1():
    return 'ydwpq'


def func2():
    return 9.0


def func3():
    return [19, 56, 41]


def func4():
    return (73, 38, 29)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
