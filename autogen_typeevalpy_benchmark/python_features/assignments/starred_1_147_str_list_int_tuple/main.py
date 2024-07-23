# Functions are assigned to variables via starred assignment
def func1():
    return 'fnlmw'


def func2():
    return [13, 34, 80]


def func3():
    return 12


def func4():
    return (52, 66, 88)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
