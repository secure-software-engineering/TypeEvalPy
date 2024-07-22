# Functions are assigned to variables via starred assignment
def func1():
    return 'nbkbc'


def func2():
    return [79, 91, 20]


def func3():
    return (19, 36, 44)


def func4():
    return 2.92

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
