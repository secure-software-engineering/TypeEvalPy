# Functions are assigned to variables via starred assignment
def func1():
    return [55, 68, 89]


def func2():
    return 77


def func3():
    return 'ppoak'


def func4():
    return (90, 49, 37)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
