# Functions are assigned to variables via starred assignment
def func1():
    return (93, 81, 81)


def func2():
    return 11.09


def func3():
    return 'bwbyc'


def func4():
    return [96, 83, 2]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
