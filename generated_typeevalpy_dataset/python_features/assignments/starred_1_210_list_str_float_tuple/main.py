# Functions are assigned to variables via starred assignment
def func1():
    return [89, 38, 21]


def func2():
    return 'foszq'


def func3():
    return 23.95


def func4():
    return (25, 44, 42)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
