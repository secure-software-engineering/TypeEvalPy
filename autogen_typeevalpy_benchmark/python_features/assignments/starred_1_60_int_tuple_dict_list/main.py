# Functions are assigned to variables via starred assignment
def func1():
    return 3


def func2():
    return (43, 29, 38)


def func3():
    return {'tjotf': 61, 'ptzld': 82, 'ecysd': 45}


def func4():
    return [32, 2, 83]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
