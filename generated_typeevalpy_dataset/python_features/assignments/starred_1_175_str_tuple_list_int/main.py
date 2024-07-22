# Functions are assigned to variables via starred assignment
def func1():
    return 'cehag'


def func2():
    return (51, 62, 41)


def func3():
    return [13, 76, 11]


def func4():
    return 39

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
