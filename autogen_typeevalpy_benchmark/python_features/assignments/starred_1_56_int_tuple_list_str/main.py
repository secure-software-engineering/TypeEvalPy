# Functions are assigned to variables via starred assignment
def func1():
    return 33


def func2():
    return (17, 61, 47)


def func3():
    return [99, 48, 57]


def func4():
    return 'jepci'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
