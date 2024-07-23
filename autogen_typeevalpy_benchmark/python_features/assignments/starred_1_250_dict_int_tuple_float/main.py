# Functions are assigned to variables via starred assignment
def func1():
    return {'onxls': 79, 'knrok': 84, 'ectvc': 8}


def func2():
    return 15


def func3():
    return (83, 19, 38)


def func4():
    return 49.4

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
