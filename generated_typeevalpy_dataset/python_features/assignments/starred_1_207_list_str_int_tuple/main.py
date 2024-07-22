# Functions are assigned to variables via starred assignment
def func1():
    return [24, 93, 34]


def func2():
    return 'mamuz'


def func3():
    return 86


def func4():
    return (47, 30, 32)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
