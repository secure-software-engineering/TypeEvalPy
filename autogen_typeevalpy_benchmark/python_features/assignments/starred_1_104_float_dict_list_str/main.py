# Functions are assigned to variables via starred assignment
def func1():
    return 5.51


def func2():
    return {'jbyzw': 37, 'unxib': 46, 'apdvy': 56}


def func3():
    return [15, 81, 83]


def func4():
    return 'mwkas'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
