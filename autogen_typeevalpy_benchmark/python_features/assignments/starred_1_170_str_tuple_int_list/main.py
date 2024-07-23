# Functions are assigned to variables via starred assignment
def func1():
    return 'geerr'


def func2():
    return (56, 7, 55)


def func3():
    return 16


def func4():
    return [73, 73, 44]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
