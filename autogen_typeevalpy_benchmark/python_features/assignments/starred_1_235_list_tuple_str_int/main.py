# Functions are assigned to variables via starred assignment
def func1():
    return [62, 30, 41]


def func2():
    return (60, 78, 17)


def func3():
    return 'dskik'


def func4():
    return 76

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
