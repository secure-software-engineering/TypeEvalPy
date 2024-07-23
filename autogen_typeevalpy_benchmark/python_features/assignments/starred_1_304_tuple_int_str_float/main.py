# Functions are assigned to variables via starred assignment
def func1():
    return (93, 31, 31)


def func2():
    return 30


def func3():
    return 'qgjau'


def func4():
    return 85.82

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
