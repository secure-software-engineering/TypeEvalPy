# Functions are assigned to variables via starred assignment
def func1():
    return 26.12


def func2():
    return {'vatgk': 26, 'kmawa': 39, 'wkjil': 12}


def func3():
    return [10, 41, 97]


def func4():
    return (61, 99, 27)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
