# Functions are assigned to variables via starred assignment
def func1():
    return 'fgami'


def func2():
    return 32.68


def func3():
    return (18, 12, 21)


def func4():
    return [50, 24, 54]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
