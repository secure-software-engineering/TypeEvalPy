# Functions are assigned to variables via starred assignment
def func1():
    return (67, 69, 16)


def func2():
    return [36, 73, 70]


def func3():
    return 79.58


def func4():
    return {'xdkib': 5, 'nkjau': 76, 'acozx': 38}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
