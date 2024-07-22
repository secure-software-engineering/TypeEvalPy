# Functions are assigned to variables via starred assignment
def func1():
    return {'txvge': 94, 'iyfdu': 86, 'ocnwb': 75}


def func2():
    return 'wlclk'


def func3():
    return (73, 52, 91)


def func4():
    return 25.51

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
