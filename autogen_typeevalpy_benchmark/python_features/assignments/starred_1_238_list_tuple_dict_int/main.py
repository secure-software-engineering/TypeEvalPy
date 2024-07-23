# Functions are assigned to variables via starred assignment
def func1():
    return [98, 8, 39]


def func2():
    return (23, 19, 9)


def func3():
    return {'dfyqs': 25, 'pfzcv': 83, 'glwlm': 64}


def func4():
    return 24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
