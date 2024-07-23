# Functions are assigned to variables via starred assignment
def func1():
    return (19, 53, 26)


def func2():
    return 19.84


def func3():
    return [28, 89, 91]


def func4():
    return 'mbruh'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
