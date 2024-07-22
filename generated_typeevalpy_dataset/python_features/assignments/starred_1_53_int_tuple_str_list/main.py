# Functions are assigned to variables via starred assignment
def func1():
    return 33


def func2():
    return (1, 88, 49)


def func3():
    return 'tznpa'


def func4():
    return [8, 57, 32]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
