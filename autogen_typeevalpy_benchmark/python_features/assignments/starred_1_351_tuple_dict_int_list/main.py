# Functions are assigned to variables via starred assignment
def func1():
    return (46, 73, 98)


def func2():
    return {'kxlfr': 47, 'kpgip': 56, 'aojuh': 100}


def func3():
    return 85


def func4():
    return [84, 48, 26]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
