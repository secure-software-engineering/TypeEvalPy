# Functions are assigned to variables via starred assignment
def func1():
    return 54


def func2():
    return [91, 31, 38]


def func3():
    return (54, 77, 3)


def func4():
    return 'tlkvs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
