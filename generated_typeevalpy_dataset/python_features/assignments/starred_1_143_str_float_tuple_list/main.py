# Functions are assigned to variables via starred assignment
def func1():
    return 'fymli'


def func2():
    return 58.24


def func3():
    return (57, 15, 100)


def func4():
    return [40, 37, 70]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
