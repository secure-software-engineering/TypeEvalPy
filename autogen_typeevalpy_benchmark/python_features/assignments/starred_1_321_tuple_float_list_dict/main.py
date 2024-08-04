# Functions are assigned to variables via starred assignment
def func1():
    return (69, 49, 16)


def func2():
    return 11.1


def func3():
    return [50, 4, 26]


def func4():
    return {'wbnet': 65, 'aiiqj': 97, 'jgtng': 33}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
