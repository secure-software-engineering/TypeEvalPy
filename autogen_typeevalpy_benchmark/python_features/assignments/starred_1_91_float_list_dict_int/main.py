# Functions are assigned to variables via starred assignment
def func1():
    return 81.93


def func2():
    return [7, 67, 83]


def func3():
    return {'ibvwl': 60, 'qkepn': 18, 'rrhib': 64}


def func4():
    return 68

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
