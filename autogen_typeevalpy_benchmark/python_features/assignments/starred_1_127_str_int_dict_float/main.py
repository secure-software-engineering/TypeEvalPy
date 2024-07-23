# Functions are assigned to variables via starred assignment
def func1():
    return 'uoixb'


def func2():
    return 65


def func3():
    return {'elpde': 27, 'lytpp': 32, 'udrqu': 7}


def func4():
    return 18.64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
