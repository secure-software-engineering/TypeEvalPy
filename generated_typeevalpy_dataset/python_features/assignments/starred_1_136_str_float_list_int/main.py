# Functions are assigned to variables via starred assignment
def func1():
    return 'bwwag'


def func2():
    return 56.23


def func3():
    return [39, 68, 34]


def func4():
    return 47

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
