# Functions are assigned to variables via starred assignment
def func1():
    return 94.78


def func2():
    return 'mgaic'


def func3():
    return 73


def func4():
    return (5, 68, 59)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
