# Functions are assigned to variables via starred assignment
def func1():
    return 'vgoup'


def func2():
    return [57, 52, 87]


def func3():
    return (32, 46, 26)


def func4():
    return 55

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
