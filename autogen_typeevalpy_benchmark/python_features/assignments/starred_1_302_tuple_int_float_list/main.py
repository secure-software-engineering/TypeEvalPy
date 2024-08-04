# Functions are assigned to variables via starred assignment
def func1():
    return (3, 74, 33)


def func2():
    return 12


def func3():
    return 18.43


def func4():
    return [92, 12, 71]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
