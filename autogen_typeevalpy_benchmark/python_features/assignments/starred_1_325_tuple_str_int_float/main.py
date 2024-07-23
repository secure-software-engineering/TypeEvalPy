# Functions are assigned to variables via starred assignment
def func1():
    return (93, 54, 45)


def func2():
    return 'bwfvo'


def func3():
    return 77


def func4():
    return 18.23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
