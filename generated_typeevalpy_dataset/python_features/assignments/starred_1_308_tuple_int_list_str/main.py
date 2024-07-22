# Functions are assigned to variables via starred assignment
def func1():
    return (73, 92, 95)


def func2():
    return 90


def func3():
    return [92, 73, 25]


def func4():
    return 'ccpwg'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
