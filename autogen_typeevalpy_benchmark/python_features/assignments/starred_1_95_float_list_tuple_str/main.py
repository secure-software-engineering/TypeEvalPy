# Functions are assigned to variables via starred assignment
def func1():
    return 22.43


def func2():
    return [38, 94, 38]


def func3():
    return (52, 90, 51)


def func4():
    return 'vejdv'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
