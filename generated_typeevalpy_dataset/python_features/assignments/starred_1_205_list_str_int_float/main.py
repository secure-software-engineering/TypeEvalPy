# Functions are assigned to variables via starred assignment
def func1():
    return [38, 30, 26]


def func2():
    return 'kyrqa'


def func3():
    return 94


def func4():
    return 47.12

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
