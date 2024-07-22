# Functions are assigned to variables via starred assignment
def func1():
    return {'pkqef': 31, 'uwchv': 58, 'tappu': 57}


def func2():
    return (74, 46, 60)


def func3():
    return [100, 78, 13]


def func4():
    return 'cwplv'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
