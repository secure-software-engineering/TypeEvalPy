# Functions are assigned to variables via starred assignment
def func1():
    return 74.29


def func2():
    return [65, 97, 97]


def func3():
    return 'zexba'


def func4():
    return (1, 68, 51)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
