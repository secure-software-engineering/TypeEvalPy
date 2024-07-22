# Functions are assigned to variables via starred assignment
def func1():
    return 'tvosl'


def func2():
    return (69, 58, 79)


def func3():
    return 26


def func4():
    return [47, 8, 26]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
