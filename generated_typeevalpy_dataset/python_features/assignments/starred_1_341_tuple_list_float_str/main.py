# Functions are assigned to variables via starred assignment
def func1():
    return (17, 57, 79)


def func2():
    return [76, 4, 8]


def func3():
    return 60.34


def func4():
    return 'tqnem'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
