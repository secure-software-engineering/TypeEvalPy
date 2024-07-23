# Functions are assigned to variables via starred assignment
def func1():
    return [69, 41, 16]


def func2():
    return (91, 24, 1)


def func3():
    return 'dlrnu'


def func4():
    return 38

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
