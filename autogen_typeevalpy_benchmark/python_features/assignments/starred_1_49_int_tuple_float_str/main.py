# Functions are assigned to variables via starred assignment
def func1():
    return 73


def func2():
    return (56, 60, 96)


def func3():
    return 78.1


def func4():
    return 'vitas'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
