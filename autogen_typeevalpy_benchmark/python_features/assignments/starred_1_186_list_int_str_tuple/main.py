# Functions are assigned to variables via starred assignment
def func1():
    return [95, 85, 69]


def func2():
    return 44


def func3():
    return 'ncqaj'


def func4():
    return (93, 14, 73)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
