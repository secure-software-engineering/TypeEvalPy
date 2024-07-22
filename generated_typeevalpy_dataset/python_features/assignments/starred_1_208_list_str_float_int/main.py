# Functions are assigned to variables via starred assignment
def func1():
    return [17, 26, 59]


def func2():
    return 'izoxu'


def func3():
    return 95.62


def func4():
    return 9

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
