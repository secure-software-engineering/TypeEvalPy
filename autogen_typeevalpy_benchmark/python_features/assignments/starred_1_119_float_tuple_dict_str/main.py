# Functions are assigned to variables via starred assignment
def func1():
    return 57.05


def func2():
    return (67, 70, 5)


def func3():
    return {'wslum': 99, 'hwzbv': 41, 'reefy': 65}


def func4():
    return 'kgspl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
