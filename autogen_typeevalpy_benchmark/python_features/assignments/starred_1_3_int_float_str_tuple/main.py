# Functions are assigned to variables via starred assignment
def func1():
    return 79


def func2():
    return 53.44


def func3():
    return 'clryz'


def func4():
    return (19, 100, 32)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
