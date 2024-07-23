# Functions are assigned to variables via starred assignment
def func1():
    return 10


def func2():
    return 20.87


def func3():
    return (2, 21, 72)


def func4():
    return 'pzfli'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
