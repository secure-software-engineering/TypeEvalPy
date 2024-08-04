# Functions are assigned to variables via starred assignment
def func1():
    return [54, 90, 46]


def func2():
    return 48.81


def func3():
    return 62


def func4():
    return 'kheju'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
