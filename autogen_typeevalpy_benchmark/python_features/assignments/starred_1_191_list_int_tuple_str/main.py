# Functions are assigned to variables via starred assignment
def func1():
    return [83, 72, 69]


def func2():
    return 68


def func3():
    return (59, 32, 63)


def func4():
    return 'cbyod'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
