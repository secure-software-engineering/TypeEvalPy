# Functions are assigned to variables via starred assignment
def func1():
    return (22, 77, 24)


def func2():
    return 'cxxzu'


def func3():
    return {'tmasq': 52, 'oagek': 8, 'qatch': 65}


def func4():
    return [35, 24, 83]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
