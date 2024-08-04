# Functions are assigned to variables via starred assignment
def func1():
    return 'apkal'


def func2():
    return [79, 87, 4]


def func3():
    return {'rbcty': 91, 'luhao': 20, 'senic': 15}


def func4():
    return (96, 47, 75)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
