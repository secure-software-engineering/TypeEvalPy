# Functions are assigned to variables via starred assignment
def func1():
    return 18


def func2():
    return [14, 54, 91]


def func3():
    return (50, 94, 64)


def func4():
    return 'batcw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
