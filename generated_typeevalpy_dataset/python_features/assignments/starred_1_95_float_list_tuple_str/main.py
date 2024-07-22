# Functions are assigned to variables via starred assignment
def func1():
    return 21.54


def func2():
    return [86, 65, 72]


def func3():
    return (96, 94, 17)


def func4():
    return 'bmucu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
