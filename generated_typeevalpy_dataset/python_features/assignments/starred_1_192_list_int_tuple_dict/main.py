# Functions are assigned to variables via starred assignment
def func1():
    return [34, 77, 34]


def func2():
    return 81


def func3():
    return (87, 8, 17)


def func4():
    return {'cvkng': 46, 'tzaet': 32, 'mvozz': 3}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
