# Functions are assigned to variables via starred assignment
def func1():
    return (11, 78, 11)


def func2():
    return 95.39


def func3():
    return {'jomyk': 19, 'azcyh': 6, 'kcnpz': 77}


def func4():
    return 'kzjrz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
