# Functions are assigned to variables via starred assignment
def func1():
    return 47.41


def func2():
    return [43, 78, 9]


def func3():
    return 75


def func4():
    return {'orjuy': 88, 'acyeg': 58, 'jidur': 29}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
