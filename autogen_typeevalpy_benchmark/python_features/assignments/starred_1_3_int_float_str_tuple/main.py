# Functions are assigned to variables via starred assignment
def func1():
    return 67


def func2():
    return 50.89


def func3():
    return 'jrjtu'


def func4():
    return (32, 79, 10)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
