# Functions are assigned to variables via starred assignment
def func1():
    return {'ihqkd': 65, 'fnzmv': 10, 'kviel': 33}


def func2():
    return [8, 87, 63]


def func3():
    return 66.41


def func4():
    return (9, 23, 63)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
