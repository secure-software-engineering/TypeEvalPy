# Functions are assigned to variables via starred assignment
def func1():
    return {'hyuwc': 99, 'xelup': 88, 'flltt': 78}


def func2():
    return [58, 49, 69]


def func3():
    return 15


def func4():
    return (96, 87, 49)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
