# Functions are assigned to variables via starred assignment
def func1():
    return 26


def func2():
    return 'iuivu'


def func3():
    return (37, 31, 34)


def func4():
    return [42, 40, 29]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
