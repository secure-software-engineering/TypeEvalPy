# Functions are assigned to variables via starred assignment
def func1():
    return 'wqvqt'


def func2():
    return 45


def func3():
    return (12, 49, 86)


def func4():
    return [7, 40, 12]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
