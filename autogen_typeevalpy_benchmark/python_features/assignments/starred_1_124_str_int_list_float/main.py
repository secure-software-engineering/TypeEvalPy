# Functions are assigned to variables via starred assignment
def func1():
    return 'rqmyk'


def func2():
    return 84


def func3():
    return [49, 80, 73]


def func4():
    return 78.13

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
