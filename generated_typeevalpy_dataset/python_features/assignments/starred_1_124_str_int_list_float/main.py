# Functions are assigned to variables via starred assignment
def func1():
    return 'ejovd'


def func2():
    return 85


def func3():
    return [37, 50, 92]


def func4():
    return 19.17

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()