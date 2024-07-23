# Functions are assigned to variables via starred assignment
def func1():
    return (2, 90, 78)


def func2():
    return 'sneih'


def func3():
    return {'zhvsz': 87, 'sfffq': 66, 'ghary': 18}


def func4():
    return 15

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
