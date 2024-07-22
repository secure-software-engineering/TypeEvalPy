# Functions are assigned to variables via starred assignment
def func1():
    return [92, 65, 71]


def func2():
    return {'eiyiu': 4, 'uzasu': 61, 'yapji': 65}


def func3():
    return 15


def func4():
    return (68, 17, 5)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
