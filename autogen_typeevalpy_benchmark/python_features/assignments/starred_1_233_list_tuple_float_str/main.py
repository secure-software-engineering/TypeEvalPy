# Functions are assigned to variables via starred assignment
def func1():
    return [35, 65, 64]


def func2():
    return (92, 93, 20)


def func3():
    return 92.98


def func4():
    return 'ftojn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
