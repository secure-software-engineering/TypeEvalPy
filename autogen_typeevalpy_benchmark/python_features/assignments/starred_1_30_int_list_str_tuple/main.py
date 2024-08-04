# Functions are assigned to variables via starred assignment
def func1():
    return 8


def func2():
    return [8, 93, 5]


def func3():
    return 'pnpgo'


def func4():
    return (67, 15, 94)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
