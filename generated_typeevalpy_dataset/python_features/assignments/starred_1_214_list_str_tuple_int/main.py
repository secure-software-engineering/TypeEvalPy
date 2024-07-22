# Functions are assigned to variables via starred assignment
def func1():
    return [56, 9, 90]


def func2():
    return 'wxpoe'


def func3():
    return (3, 75, 39)


def func4():
    return 15

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
