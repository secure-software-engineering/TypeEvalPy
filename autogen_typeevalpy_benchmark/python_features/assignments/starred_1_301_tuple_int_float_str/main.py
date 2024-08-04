# Functions are assigned to variables via starred assignment
def func1():
    return (95, 37, 37)


def func2():
    return 2


def func3():
    return 73.94


def func4():
    return 'efugq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
