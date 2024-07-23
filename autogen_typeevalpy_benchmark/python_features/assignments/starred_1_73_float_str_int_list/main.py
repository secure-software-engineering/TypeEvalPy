# Functions are assigned to variables via starred assignment
def func1():
    return 19.06


def func2():
    return 'yasjo'


def func3():
    return 51


def func4():
    return [78, 58, 66]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
