# Functions are assigned to variables via starred assignment
def func1():
    return [32, 17, 42]


def func2():
    return 10.49


def func3():
    return (4, 63, 91)


def func4():
    return 'cyiwb'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
