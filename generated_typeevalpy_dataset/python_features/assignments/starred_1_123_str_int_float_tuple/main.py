# Functions are assigned to variables via starred assignment
def func1():
    return 'crxcm'


def func2():
    return 79


def func3():
    return 76.18


def func4():
    return (53, 97, 58)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
