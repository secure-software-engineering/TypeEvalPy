# Functions are assigned to variables via starred assignment
def func1():
    return 39.44


def func2():
    return 49


def func3():
    return (69, 73, 50)


def func4():
    return {'pxyfo': 98, 'ugaom': 45, 'pqkfv': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
