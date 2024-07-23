# Functions are assigned to variables via starred assignment
def func1():
    return 'sgtad'


def func2():
    return [29, 73, 52]


def func3():
    return 77.61


def func4():
    return 91

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
