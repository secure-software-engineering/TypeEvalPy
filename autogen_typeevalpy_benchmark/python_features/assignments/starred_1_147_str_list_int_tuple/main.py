# Functions are assigned to variables via starred assignment
def func1():
    return 'uedap'


def func2():
    return [99, 79, 7]


def func3():
    return 63


def func4():
    return (52, 89, 31)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
