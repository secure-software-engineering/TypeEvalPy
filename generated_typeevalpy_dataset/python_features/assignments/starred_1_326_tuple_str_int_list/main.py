# Functions are assigned to variables via starred assignment
def func1():
    return (72, 19, 47)


def func2():
    return 'mzgmd'


def func3():
    return 12


def func4():
    return [46, 26, 6]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
