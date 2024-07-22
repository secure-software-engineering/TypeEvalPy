# Functions are assigned to variables via starred assignment
def func1():
    return 'wutuy'


def func2():
    return (86, 4, 40)


def func3():
    return 81.67


def func4():
    return 83

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
