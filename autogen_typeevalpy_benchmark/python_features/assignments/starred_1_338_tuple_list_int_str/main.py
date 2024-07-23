# Functions are assigned to variables via starred assignment
def func1():
    return (61, 30, 36)


def func2():
    return [44, 94, 48]


def func3():
    return 58


def func4():
    return 'spzbq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
