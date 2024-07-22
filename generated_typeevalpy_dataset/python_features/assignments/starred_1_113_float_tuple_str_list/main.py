# Functions are assigned to variables via starred assignment
def func1():
    return 79.59


def func2():
    return (28, 94, 40)


def func3():
    return 'susly'


def func4():
    return [97, 90, 96]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
