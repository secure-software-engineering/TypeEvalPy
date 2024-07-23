# Functions are assigned to variables via starred assignment
def func1():
    return (23, 55, 67)


def func2():
    return 81.37


def func3():
    return [24, 83, 65]


def func4():
    return {'hsgge': 83, 'wmmqz': 80, 'dipll': 95}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
