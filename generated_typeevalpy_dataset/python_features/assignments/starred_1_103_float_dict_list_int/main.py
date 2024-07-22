# Functions are assigned to variables via starred assignment
def func1():
    return 72.69


def func2():
    return {'mlwqj': 1, 'rsolw': 94, 'jbbxh': 72}


def func3():
    return [31, 6, 12]


def func4():
    return 89

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
