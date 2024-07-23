# Functions are assigned to variables via starred assignment
def func1():
    return {'usrda': 50, 'ransz': 52, 'hvveg': 3}


def func2():
    return [40, 72, 80]


def func3():
    return (21, 34, 38)


def func4():
    return 59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
