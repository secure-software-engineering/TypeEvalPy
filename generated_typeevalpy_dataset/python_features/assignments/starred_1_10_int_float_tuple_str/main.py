# Functions are assigned to variables via starred assignment
def func1():
    return 9


def func2():
    return 79.78


def func3():
    return (58, 86, 17)


def func4():
    return 'xsblc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
