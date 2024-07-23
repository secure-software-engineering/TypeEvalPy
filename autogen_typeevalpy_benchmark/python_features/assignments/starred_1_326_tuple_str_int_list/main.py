# Functions are assigned to variables via starred assignment
def func1():
    return (69, 61, 9)


def func2():
    return 'lhgdx'


def func3():
    return 20


def func4():
    return [51, 53, 91]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
