# Functions are assigned to variables via starred assignment
def func1():
    return 'wainp'


def func2():
    return (26, 97, 19)


def func3():
    return [74, 54, 83]


def func4():
    return 69.09

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
