# Functions are assigned to variables via starred assignment
def func1():
    return [90, 84, 16]


def func2():
    return 'fmvph'


def func3():
    return 84


def func4():
    return (18, 78, 38)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
