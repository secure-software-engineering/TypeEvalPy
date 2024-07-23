# Functions are assigned to variables via starred assignment
def func1():
    return [14, 54, 23]


def func2():
    return (85, 88, 9)


def func3():
    return 33.73


def func4():
    return 'ncwhn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
