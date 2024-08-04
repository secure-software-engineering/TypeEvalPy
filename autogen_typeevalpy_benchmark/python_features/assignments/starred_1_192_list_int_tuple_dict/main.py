# Functions are assigned to variables via starred assignment
def func1():
    return [92, 40, 29]


def func2():
    return 67


def func3():
    return (87, 83, 6)


def func4():
    return {'vpotf': 2, 'yqqdm': 77, 'wyqso': 9}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
