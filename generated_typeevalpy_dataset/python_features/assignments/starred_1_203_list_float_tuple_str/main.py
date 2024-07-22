# Functions are assigned to variables via starred assignment
def func1():
    return [20, 86, 79]


def func2():
    return 17.32


def func3():
    return (68, 54, 78)


def func4():
    return 'sfgrk'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
