# Functions are assigned to variables via starred assignment
def func1():
    return 54


def func2():
    return (83, 89, 25)


def func3():
    return [24, 16, 23]


def func4():
    return 'uolxp'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
