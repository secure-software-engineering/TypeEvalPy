# Functions are assigned to variables via starred assignment
def func1():
    return [39, 80, 60]


def func2():
    return 67


def func3():
    return (64, 22, 78)


def func4():
    return 'zjmik'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
