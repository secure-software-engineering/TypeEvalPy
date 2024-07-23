# Functions are assigned to variables via starred assignment
def func1():
    return 70


def func2():
    return [24, 46, 22]


def func3():
    return (30, 57, 8)


def func4():
    return {'tcwlj': 43, 'mnvkb': 6, 'yvgpx': 94}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
