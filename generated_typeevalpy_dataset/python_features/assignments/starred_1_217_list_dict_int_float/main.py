# Functions are assigned to variables via starred assignment
def func1():
    return [7, 62, 48]


def func2():
    return {'yayye': 53, 'kbyse': 51, 'hikvi': 80}


def func3():
    return 66


def func4():
    return 94.97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
