# Functions are assigned to variables via starred assignment
def func1():
    return (7, 18, 54)


def func2():
    return 'xjqym'


def func3():
    return [11, 44, 67]


def func4():
    return 56.48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
