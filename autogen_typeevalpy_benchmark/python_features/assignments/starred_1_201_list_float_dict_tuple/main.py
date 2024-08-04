# Functions are assigned to variables via starred assignment
def func1():
    return [66, 13, 29]


def func2():
    return 25.38


def func3():
    return {'ygiqv': 48, 'fefiv': 25, 'dtyao': 92}


def func4():
    return (59, 21, 8)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
