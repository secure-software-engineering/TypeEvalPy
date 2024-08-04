# Functions are assigned to variables via starred assignment
def func1():
    return 72.61


def func2():
    return 'oicku'


def func3():
    return (78, 32, 2)


def func4():
    return [99, 61, 77]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
