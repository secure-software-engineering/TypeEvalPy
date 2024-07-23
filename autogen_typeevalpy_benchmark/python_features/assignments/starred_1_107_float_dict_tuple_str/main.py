# Functions are assigned to variables via starred assignment
def func1():
    return 54.36


def func2():
    return {'vcrcl': 80, 'gqodu': 45, 'lbpon': 45}


def func3():
    return (70, 78, 88)


def func4():
    return 'xysnl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
