# Functions are assigned to variables via starred assignment
def func1():
    return 51


def func2():
    return 49.34


def func3():
    return [99, 94, 57]


def func4():
    return {'afqrw': 93, 'uvlab': 87, 'dudvv': 67}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
