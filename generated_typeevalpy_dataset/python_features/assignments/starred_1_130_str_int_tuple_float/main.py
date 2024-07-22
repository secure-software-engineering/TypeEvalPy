# Functions are assigned to variables via starred assignment
def func1():
    return 'apuyz'


def func2():
    return 58


def func3():
    return (84, 88, 91)


def func4():
    return 94.53

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
