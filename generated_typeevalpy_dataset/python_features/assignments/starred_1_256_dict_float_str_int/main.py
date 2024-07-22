# Functions are assigned to variables via starred assignment
def func1():
    return {'wtbko': 3, 'soaqi': 66, 'eetdb': 79}


def func2():
    return 10.17


def func3():
    return 'uslea'


def func4():
    return 64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
